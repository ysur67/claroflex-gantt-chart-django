from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers

from projects.models import Project, ProjectTask


class ProjectTaskSerializer(serializers.ModelSerializer):
    id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = ProjectTask
        fields = (
            'id',
            'user',
            'description',
            'start_date',
            'close_date',
            'related_task',
        )

    def validate(self, attrs):
        if attrs['close_date'] < attrs['start_date']:
            raise serializers.ValidationError({
                'close_date': _('Дата старта задачи не может быть меньше даты завершения')
            })
        return attrs

    def create(self, validated_data):
        task_id = validated_data.pop('id', 'no')
        # на фронте геренирурется рандомная строка для ид, это значит новый объект
        try:
            task_id = int(task_id)
        except ValueError:
            task_id = None
        if task_id:
            task = ProjectTask.objects.filter(id=task_id)
            task.update(**validated_data)
            return task.first()
        else:
            return super().create(validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    tasks = ProjectTaskSerializer(many=True)
    responsible_user_name = serializers.CharField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        tasks_data = validated_data.pop('tasks', [])
        project = super().create(validated_data)
        for task_data in tasks_data:
            task_data['project'] = project
            del task_data['id']
            ProjectTask.objects.create(**task_data)
        return project

    def update(self, instance, validated_data):
        with transaction.atomic():
            tasks_data = validated_data.pop('tasks', [])
            instance = super().update(instance, validated_data)
            tasks_ids = set()
            for task_data in tasks_data:
                task_data['project'] = instance
                task = ProjectTaskSerializer().create(validated_data=task_data)
                tasks_ids.add(task.id)
                if task_data.get('id'):
                    tasks_ids.add(task_data['id'])
        return instance

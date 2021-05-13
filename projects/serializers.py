from os import read
import re
from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers

from projects.models import Project, ProjectTask, ProjectComment, TaskComment, Comment
from django.contrib.auth.models import User
from rest_framework.settings import api_settings


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
            if tasks_ids:
                instance.tasks.exclude(id__in=tasks_ids).delete()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):
    user_left = UserSerializer(read_only=True)
    date = serializers.DateTimeField(required=False, format='%d.%m.%Y %H:%M:%S')

    serialized_class_title = ''
    serialized_class = ProjectComment
    related_class = ''
    request_id = ''

    class Meta:
        model = Comment
        fields = '__all__'
        set_timezone = 'date'

    def validate(self, attrs):
        if not self.request_id:
            return attrs

        request_id = self.initial_data[self.request_id]
        objects = self.related_class.objects.filter(id=request_id)
        if not objects.exists():
            raise serializers.ValidationError({
                self.request_id: _('Объект не найден')
            })

        return attrs

    def create(self, validated_data):
        data = validated_data.copy()
        if self.related_class:
            obj_id = self.initial_data[self.request_id]
            data[self.serialized_class_title] = self.related_class.objects.get(id=obj_id)
        data['user_left'] = self.context['request'].user
        data['comment_text'] = validated_data.pop('comment_text', [])
        instance = self.serialized_class.objects.create(**data)
        return instance

class ProjectCommentSerializer(CommentSerializer):
    project = ProjectSerializer(read_only=True)

    serialized_class_title = 'project'
    serialized_class = ProjectComment
    related_class = Project
    request_id = 'project_id'

    class Meta:
        model = ProjectComment
        fields = '__all__'


class TaskCommentSerializer(CommentSerializer):
    task = ProjectTaskSerializer(read_only=True)

    serialized_class_title = 'task'
    serialized_class = TaskComment
    related_class = ProjectTask
    request_id = 'task_id'

    class Meta:
        model = TaskComment
        fields = '__all__'

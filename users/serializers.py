from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    key = serializers.CharField(source='pk')

    class Meta:
        model = get_user_model()
        fields = (
            'value',
            'key',
        )

    def get_value(self, obj):
        return f"{obj.first_name} {obj.last_name}" if obj.first_name else obj.username

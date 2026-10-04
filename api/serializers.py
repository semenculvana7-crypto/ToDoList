from rest_framework import serializers
from tasks.models import Task,Profile


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']

    def validate_tittle(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                'Название задачи не может быть пустым'
            )
        return value

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]

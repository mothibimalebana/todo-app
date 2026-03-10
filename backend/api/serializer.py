from rest_framework import serializers
from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created', 'updated']
from rest_framework import serializers
from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    complete = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'updated', 'created', 'complete']

class TaskCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id']
        read_only_fields = ['title', 'description', 'updated', 'created', 'complete']
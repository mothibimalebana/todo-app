from rest_framework import serializers
from todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user', 'created', 'updated']
        read_only_fields = ['user']
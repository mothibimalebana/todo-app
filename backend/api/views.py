from django.contrib.auth.models import User
from todo.models import Task
from api.serializer import TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class TaskList(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        userID = self.request.user.id
        return Task.objects.filter(user=userID)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        userID = self.request.user.id
        return Task.objects.filter(user=userID)

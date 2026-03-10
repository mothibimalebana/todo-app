from todo.models import Task
from api.serializer import TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

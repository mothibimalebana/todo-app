from todo.models import Task
from api.serializer import TaskSerializer, TaskCompleteSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

class TaskCompleteUpdate(generics.UpdateAPIView):
    serializer_class = TaskCompleteSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    
    def perform_update(self, serializer):
        serializer.instance.complete = not(serializer.instance.complete)
        serializer.save()
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error':'user name is taken, choose another'},
                status=400
            )

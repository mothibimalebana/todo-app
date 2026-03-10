from django.contrib import admin
from django.urls import path, include
from api.views import TaskList

urlpatterns = [
    path('tasks/', TaskList.as_view()),
]
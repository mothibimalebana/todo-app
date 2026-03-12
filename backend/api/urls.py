from django.contrib import admin
from django.urls import path, include
from api.views import TaskList, TaskDetail, TaskCompleteUpdate, signup, login

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:pk>', TaskDetail.as_view()),
    path('tasks/<int:pk>/complete', TaskCompleteUpdate.as_view()),
    path('signup/', signup),
    path('login/', login),
]
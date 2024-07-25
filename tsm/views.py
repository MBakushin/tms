from django.shortcuts import render
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer
from .tasks import process_task


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        process_task.delay(task.id)

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Task
from ..serializers import TaskSerializer


class TaskViewSetTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description'
        )
        self.url = reverse('task-list')

    def test_get_all_tasks(self):
        response = self.client.get(self.url)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_task(self):
        data = {
            'title': 'New Task',
            'description': 'New Description'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=response.data['id']).title, 'New Task')

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'status': 'completed'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.status, 'completed')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

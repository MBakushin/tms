from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Task


class TaskSearchTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(
            title='Searchable Task',
            description='Searchable Description'
        )

    def test_search_task(self):
        url = reverse('task-search') + '?q=Searchable'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertEqual(response.data[0]['title'], 'Searchable Task')

from django.test import TestCase

from ..models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description'
        )

    def test_task_creation(self):
        self.assertIsInstance(self.task, Task)
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.status, 'pending')

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), self.task.title)

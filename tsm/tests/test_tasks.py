from django.test import TestCase
from unittest.mock import patch

from ..models import Task
from ..tasks import process_task


class TaskProcessingTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description'
        )

    @patch('tasks.tasks.time.sleep', return_value=None)
    def test_task_processing(self, _):
        process_task(self.task.id)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, 'completed')

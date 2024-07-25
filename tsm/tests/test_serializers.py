from django.test import TestCase

from ..models import Task
from ..serializers import TaskSerializer


class TaskSerializerTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description'
        )
        self.serializer = TaskSerializer(instance=self.task)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'title', 'description', 'status', 'created_at'])

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], 'Test Task')

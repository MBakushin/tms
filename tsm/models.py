from django.db import models

from elasticsearch_dsl import Document, Text, Date


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('queued', 'Queued'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='queued')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskDocument(Document):
    title = Text()
    description = Text()
    created_at = Date()

    class Index:
        name = 'tasks'

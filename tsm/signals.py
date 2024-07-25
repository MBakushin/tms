from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Task, TaskDocument


@receiver(post_save, sender=Task)
def index_task(sender, instance, **kwargs):
    task_doc = TaskDocument(
        meta={'id': instance.id},
        title=instance.title,
        description=instance.description,
        created_at=instance.created_at
    )
    task_doc.save()

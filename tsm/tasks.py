import time
import logging
from celery import shared_task

from .models import Task



logger = logging.getLogger(__name__)


@shared_task
def process_task(task_id):
    task = Task.objects.get(id=task_id)
    logger.info(f'Starting task processing: {task_id}')
    time.sleep(10)
    task.status = 'completed'
    task.save()
    logger.info(f'Task completed: {task_id}')

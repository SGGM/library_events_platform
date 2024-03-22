import time

from celery import shared_task

from .models import Event


@shared_task
def task_execute(job_params):
    event = Event.objects.get(pk=job_params["db_id"])

    time.sleep(60)

    event.created = True

    event.save()

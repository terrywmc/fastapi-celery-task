import os
import time

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
celery.conf.result_expires = 60

@celery.task(name="task_1")
def task_1(input:int):
    time.sleep(10)
    return input


@celery.task(name="task_2")
def task_2(input:int):
    time.sleep(10)
    return input*2
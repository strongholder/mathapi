from celery import Celery

from mathapi.app import create_app
from mathapi.celery import init_celery, tasks

celery = init_celery(create_app(), Celery())

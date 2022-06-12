import os

# Set the default Django settings module for the 'celery' program.
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.broker_url = 'redis://redis:6379/0'

app.conf.beat_schedule = {
    # Executes every minute.
    'add-every-minute': {
        'task': 'djangoApp.tasks.update_counter',
        'schedule': crontab(minute='*/1'),
    },
}

from django.db.models import F

from djangoApp.models import Counter
from djangoProject.celery import app


@app.task
def update_counter():
    getattr(Counter, 'objects').update(value=F('value')+1)

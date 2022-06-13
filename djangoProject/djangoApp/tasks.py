from django.db.models import F, Q

from djangoApp.models import Counter, Project
from djangoProject.celery import app
from utils.get_projects import get_projects


@app.task
def update_counter():
    getattr(Counter, 'objects').update(value=F('value')+1)


@app.task
def sync_projects():
    response = get_projects()
    if response.ok:
        project_list = response.json()
        database_project_id_list = (
            getattr(Project, 'objects')
            .filter(id__in=[project['id'] for project in project_list['value'] if project['state'] != 'deleted'])
            .values_list('id', flat=True)
        )
        getattr(Project, 'objects').filter(
            ~Q(id__in=[project['id'] for project in project_list['value']])
            | Q(id__in=[project['id'] for project in project_list['value'] if project['state'] == 'deleted'])
        ).delete()
        create_project_list = [
            Project(**project)
            for project in project_list['value']
            if project['id'] not in database_project_id_list
        ]
        if create_project_list:
            getattr(Project, 'objects').bulk_create(create_project_list)

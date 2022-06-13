from djangoProject.settings import AZURE_ORG_URL
from utils.get import get


def get_projects():
    url = f'{AZURE_ORG_URL}/_apis/projects'
    response = get(url)
    return response

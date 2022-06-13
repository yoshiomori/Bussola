import requests

from djangoProject.settings import AZURE_TOKEN


def get(url):
    params = {'api-version': '7.0'}
    headers = {
        'Authorization': f'Basic {AZURE_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, params, headers=headers)
    return response

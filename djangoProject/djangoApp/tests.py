from unittest import TestCase
from unittest.mock import patch, MagicMock

from django import setup

from djangoApp.constants.project_response import PROJECT_RESPONSE

setup()

response = MagicMock()


# @patch('requests.get', return_value=response)
class Test(TestCase):
    def test_sync_projects(self):
        response.json.return_value = PROJECT_RESPONSE
        response.status_code = 200
        response.ok = True
        from djangoApp.tasks import sync_projects
        sync_projects()
        self.fail('Not implemented')

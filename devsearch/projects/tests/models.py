from django.test import TestCase
from projects.models import Project

# Create your tests here.

class ModelTests(TestCase):
    def test_model_project_str(self):
        project_object = Project.objects.create(title='New Project Title')
        self.assertEqual(str(project_object), 'New Project Title')
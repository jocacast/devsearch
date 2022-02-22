from django.test import TestCase
from django.urls import reverse, resolve
from projects.views import createProject, project

# Create your tests here.

class URLTests(TestCase):
    def test_create_project(self):
        url = reverse('create-project')
        self.assertEqual(resolve(url).func, createProject)
    
    def test_project(self):
        url = reverse('project', kwargs={'pk':4} )
        self.assertEqual(resolve(url).func, project)

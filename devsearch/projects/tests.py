from django.test import TestCase
from django.urls import reverse, resolve
from .views import createProject, project

# Create your tests here.

class URLTests(TestCase):
    def test_create_project(self):
        url = reverse('create-project')
        self.assertEqual(resolve(url).func, createProject)
    
    def test_project(self):
        url = reverse('project', kwargs={'pk':4} )
        print(resolve(url))
        self.assertEqual(resolve(url).func, project)

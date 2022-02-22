from django.test import TestCase, Client
from django.urls import reverse, resolve
from projects.models import Project, Tag
import datetime

# Create your tests here.

class ViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.projects_url = reverse('projects')
        self.tag = Tag.objects.create(id = 'e975bfee-568c-4aae-bcc8-873f330e46a6', created = datetime.datetime.now(), name = 'Test Tag')
        self.tag_url = reverse('tag', kwargs={'pk':'e975bfee-568c-4aae-bcc8-873f330e46a6'} )
        

    def test_get_projects (self):
        response = self.client.get(self.projects_url)
        #print(f'{response}')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'projects\projects.html')
    
    def test_tag_detail(self):
        response = self.client.get(self.tag_url)
        print(resolve(self.tag_url))
        print(f'{self.tag.id} , {response}')
        self.assertEqual(response.status_code,200)
    




        
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Create your tests here.

class Landing_Page_TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
         url = reverse('index')
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'index.html')
         self.assertContains(response, 'Getting Started with Python on Heroku')

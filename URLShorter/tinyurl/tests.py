from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from .models import URLStore


# Create your tests here.

class TestView(TestCase):
    def test_home_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'url_template.html')

    def test_tinyurl_status_code(self):
        response = self.client.get(reverse('tiny'))
        self.assertEqual(response.status_code, 200)

    def test_tinyurl_template(self):
        response = self.client.get(reverse('tiny'))
        self.assertTemplateUsed(response, 'url_template.html')

    @patch('tinyurl.views.shorten_url')
    def test_shorten_url_error(self, mock_short):
        mock_short.side_effect = Exception("Error in shortening")
        response = self.client.post(reverse('tiny'), data={'inurl': 'https://builder11.zety.com/dashboard'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Failed to shorten url")


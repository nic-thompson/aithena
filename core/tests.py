from django.test import TestCase
from django.urls import reverse

class CoreTests(TestCase):
    def test_home_view_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_returns_expected_json(self):
        response = self.client.get(reverse('home'))
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"message": "Welcome to Aithena!"}
        )

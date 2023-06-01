from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase

from decouple import config


class APiKeyAutenticationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_api_key(self):
        api_key = config('OPENAI_API_KEY')

        response = self.client.post('/api/authentication', {'api_key': api_key}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'response': 'valid_api_key'})

    def test_invalid_api_key(self):
        api_key = 'api_key'

        response = self.client.post('/api/authentication', {'api_key': api_key}, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'response': 'invalid_api_key'})

    def test_missing_api_key(self):
        response = self.client.post('/api/authentication', {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'response': 'invalid_api_key'})

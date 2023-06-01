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


class UploadCSVAPIViewTest(APITestCase):
    def test_valid_csv_file(self):
        csv_file = open('static\csv\data_test.csv', 'rb')
        response = self.client.post('/api/uploadcsv', {'file': csv_file}, format='multipart')

        expected_processed_data = [
            ['jesus', 'suyon', 29, 'yes'],
            ['chari', 'soplapuco', 26, 'yes'],
            ['carlos', 'sosa', 26, 'no'],
            ['beto', 'santillana', 30, 'no'],
            ['maria', 'dominguez', 43, 'yes'],
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], expected_processed_data)

    def test_missing_file(self):
        response = self.client.post('/api/uploadcsv', {}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'No file provided')

    def test_invalid_file_format(self):
        invalid_file = open('static\csv\invalid_test.txt', 'rb')
        response = self.client.post('/api/uploadcsv', {'file': invalid_file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'The file must be in CSV format')
   
    def test_malformed_data(self):
        malformed_file = open('static\csv\malformed_test.csv', 'rb')
        response = self.client.post('/api/uploadcsv', {'file': malformed_file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'The data is malformed or missing data in the rows.')

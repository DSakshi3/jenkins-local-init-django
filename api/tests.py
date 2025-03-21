from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'completed': False
        }
        self.response = self.client.post(
            '/api/tasks/',
            self.task_data,
            format='json'
        )

    def test_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
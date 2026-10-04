from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class TaskAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345678'
        )

        self.client.force_authenticate(user=self.user)

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_task(self):
        data = {
            'tittle': 'Тестовая задача',
            'description': 'Создана через API',
            'completed': False,
        }

        response = self.client.post('/api/tasks/', data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(response.data['tittle'], 'Тестовая задача')

    def test_user_sees_only_own_tasks(self):
        from tasks.models import Task

        other_user = User.objects.create_user(
            username='otheruser',
            password='12345678'
        )

        Task.objects.create(
            tittle='Чужая задача',
            description='Не должна отображаться',
            completed=False,
            user=other_user
        )

        response = self.client.get('/api/tasks/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['count'], 0)

    def test_update_task(self):
        from tasks.models import Task

        task = Task.objects.create(
            tittle='Старая задача',
            description='Старое описание',
            completed=False,
            user=self.user
        )

        response = self.client.patch(
            f'/api/tasks/{task.id}/',
            {'completed': True}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        task.refresh_from_db()

        self.assertTrue(task.completed)

    def test_delete_task(self):
        from tasks.models import Task

        task = Task.objects.create(
            tittle='Задача для удаления',
            description='Удалить',
            completed=False,
            user=self.user
        )

        response = self.client.delete(
            f'/api/tasks/{task.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Task.objects.filter(id=task.id).exists()
        )

    def test_unauthorized(self):
        self.client.force_authenticate(user=None)

        response = self.client.get('/api/tasks/')

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )
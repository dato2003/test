

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Notes

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_registration(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        self.client.post(self.register_url, data, format='json')

        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class NoteTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.notes_create_url = reverse('notes-create')
        self.note_manage_url = reverse('notes-manage')

    def test_note_creation(self):
        
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Test Note', 'content': 'This is a test note'}
        response = self.client.post(self.notes_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_note_retrieval(self):
        
        self.client.login(username='testuser', password='testpassword')
        note = Notes.objects.create(title='Test Note', content='This is a test note')
        response = self.client.get(reverse('notes-manage', kwargs={'pk': note.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


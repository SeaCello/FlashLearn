from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.test import Client, TestCase
from .models import UserFlashcard

class FlashcardViewsTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')
    
    def test_create_flashcards_get(self):
        """Teste de GET dos flashcards"""
        url = reverse('flashcards:create_flashcards')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('flashcards', response.context)
    
    def test_create_flashcards_upload(self):
        """Teste de upload de arquivo"""
        url = reverse('flashcards:create_flashcards')
        file = SimpleUploadedFile("test.pdf", b"file_content", content_type="application/pdf")
        response = self.client.post(url, {'file': file}, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertIn('flashcards', response.context)
    
    def test_create_flashcards_ajax_update(self):
        """Teste de update de flashcards"""
        url = reverse('flashcards:create_flashcards')
        data = {
            'title': ['Flashcard 1'],
            'content': ['Conteúdo do flashcard'],
            'flashcard_id': ['1']
        }
        response = self.client.post(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'success')
    
    def test_download_pdf_with_flashcards(self):
        UserFlashcard.objects.create(user=self.user, title='Test', content='Content')
        url = reverse('flashcards:download_pdf')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

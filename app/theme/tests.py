from django.test import TestCase, Client
from django.urls import reverse

class DarkModeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_toggle_dark_mode(self):
        """Verifica se a mudança de tema é armazenada na sessão."""
        session = self.client.session
        session['is_dark_theme'] = False
        session.save()

        response = self.client.get(reverse('change-mode'))
        self.assertRedirects(response, '/')  # Verifica redirecionamento

        session = self.client.session  # Recarrega a sessão
        self.assertTrue(session['is_dark_theme'])  # O tema deve estar ativado

        response = self.client.get(reverse('change-mode'))
        session = self.client.session
        self.assertFalse(session['is_dark_theme'])  # O tema deve estar desativado

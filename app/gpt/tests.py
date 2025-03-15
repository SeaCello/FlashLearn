from django.test import TestCase
import unittest
from unittest.mock import patch, MagicMock
from .api import generate_flashcards
from openai import OpenAI

class TestGenerateFlashcards(unittest.TestCase):
    
    @patch("gpt.api.client.chat.completions.create")
    def test_generate_flashcards_success(self, mock_openai):
        """Testa se os flashcards são gerados corretamente quando a API retorna uma resposta válida."""
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content="""
            - Pergunta 1 | Resposta 1
            - Pergunta 2 | Resposta 2
            - Pergunta 3 | Resposta 3
            - Pergunta 4 | Resposta 4
            """))
        ]
        mock_openai.return_value = mock_response

        text = "Texto de exemplo para flashcards."
        flashcards = generate_flashcards(text)

        expected_flashcards = [
            {'title': 'Pergunta 1', 'content': 'Resposta 1'},
            {'title': 'Pergunta 2', 'content': 'Resposta 2'},
            {'title': 'Pergunta 3', 'content': 'Resposta 3'},
            {'title': 'Pergunta 4', 'content': 'Resposta 4'}
        ]

        self.assertEqual(flashcards, expected_flashcards)
    
    @patch("gpt.api.client.chat.completions.create")
    def test_generate_flashcards_invalid_format(self, mock_openai):
        """Testa se a função lida corretamente com um formato inesperado da API."""
        mock_response = MagicMock()
        mock_response.choices = [
            MagicMock(message=MagicMock(content="""
            - Apenas um lado
            - Outro sem separação correta
            """))
        ]
        mock_openai.return_value = mock_response

        text = "Texto de exemplo com resposta mal formatada."
        flashcards = generate_flashcards(text)

        self.assertEqual(len(flashcards), 2)
        self.assertEqual(flashcards[0]['title'], 'Flashcard')
        self.assertEqual(flashcards[1]['title'], 'Flashcard')
    
    @patch("gpt.api.client.chat.completions.create", side_effect=Exception("Erro na API"))
    def test_generate_flashcards_api_error(self, mock_openai):
        """Testa se a função levanta uma exceção quando a API falha."""
        text = "Texto de erro"
        with self.assertRaises(Exception) as context:
            generate_flashcards(text)
        
        self.assertIn("Erro ao gerar flashcards", str(context.exception))

if __name__ == "__main__":
    unittest.main()

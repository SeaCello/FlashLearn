from django.urls import path
from .views import create_flashcards, download_pdf


urlpatterns = [
    path('', create_flashcards, name='server_flashcards'), # change latter to show flashcards
    path('create/', create_flashcards, name='create_flashcards'), # create flashcards
    path('create/download_pdf', download_pdf, name='download_pdf'), # download flashcards
]

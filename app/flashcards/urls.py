from django.urls import path
from .views import create_flashcards


urlpatterns = [
    path('create/', create_flashcards, name='create_flashcards'),
]

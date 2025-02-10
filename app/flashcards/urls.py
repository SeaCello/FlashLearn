from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('', views.create_flashcards, name='flashcards'), # change latter to show flashcards
    path('create/', views.create_flashcards, name='create_flashcards'), # create flashcards
    path('create/download_pdf', views.download_pdf, name='download_pdf'), # download flashcards
]

from django.urls import path
from . import views

app_name = 'flashcards'

urlpatterns = [
    path('user/home/', views.user_flashcards_home, name='home_flashcards'), 
    path('user/flashcards/', views.meus_flashcards, name='my_flashcards'),# change latter to show flashcards
    path('user/flashcards/create', views.create_flashcards, name='create_flashcards'), # create flashcards
    path('user/flashcards/download_pdf', views.download_pdf, name='download_pdf'), # download flashcards
]

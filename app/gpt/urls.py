from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_view, name='gpt_chat'),
]

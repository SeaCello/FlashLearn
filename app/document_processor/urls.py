from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# document_processor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_document, name='upload_document'),
    path('download/<uuid:document_id>/', views.download_document, name='download_document'),
]
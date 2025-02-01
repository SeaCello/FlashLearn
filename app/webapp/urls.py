"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #to server midia files
from upload import views as upload_views #import views from upload app
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/',upload_views.UploadView.as_view() ,name='upload'),
    path('gpt/', include('gpt.urls')),  # include the urls from the gpt app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #to server midia files

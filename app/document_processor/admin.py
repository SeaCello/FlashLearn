from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'processed')
    list_filter = ('processed', 'uploaded_at')
    readonly_fields = ('id', 'uploaded_at')
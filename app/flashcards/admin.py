from django.contrib import admin
from .models import UserFlashcard

@admin.register(UserFlashcard)
class UserFlashcardAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'content', 'create_at')
    list_filter = ('user', 'create_at')
    search_fields = ('user__username', 'content', 'title')
    date_hierarchy = 'create_at'
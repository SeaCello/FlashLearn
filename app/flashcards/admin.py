from django.contrib import admin
from .models import UserFlashcard

@admin.register(UserFlashcard)
class UserFlashcardAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'create_at')
    list_filter = ('user', 'create_at')
    search_fields = ('user__username', 'content')
    date_hierarchy = 'create_at'
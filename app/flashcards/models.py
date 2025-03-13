from django.db import models
from django.contrib.auth.models import User



class UserFlashcard(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_flashcards')
    title = models.CharField(max_length= 255, blank=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_at']
        
    def __str__(self):
        return f"Flashcard de {self.user.username} - {self.create_at.strftime('%d/%m/%Y')}"
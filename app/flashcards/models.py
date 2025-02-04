from django.db import models

# Create your models here.
class FlashCard(models.Model):
    ## Define the fields of the FlashCard model
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
    
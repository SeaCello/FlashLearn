from django.db import models

# Create your models here.
class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return self.file.name # show the file name in the admin interface
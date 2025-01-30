from django.db import models
import uuid

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    output_file = models.FileField(upload_to='outputs/', null=True, blank=True)

    def __str__(self):
        return f"Document {self.id}"
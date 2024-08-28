from django.db import models
import uuid
# Create your models here.

class Post(models.Model):
    title = models.CharField( max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image_front = models.ImageField(null=True, blank=True, default='')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
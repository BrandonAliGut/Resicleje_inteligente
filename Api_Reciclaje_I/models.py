from typing import Any
from django.db import models
from cloudinary.models import CloudinaryField



import datetime
# Create your models here.


class Category(models.Model):
    name        = models.CharField(max_length=50, blank=False)
    img         = CloudinaryField("ImageCategory", blank=True)
    information = models.TextField()
    created_at  = models.DateField( auto_now_add=True, editable=False)
    updated_at   = models.DateField(default=datetime.datetime.now())
    is_active       = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
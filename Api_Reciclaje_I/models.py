from typing import Any
from django.db import models
from cloudinary.models import CloudinaryField
import datetime
# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=50, blank=False)
    img= CloudinaryField("Img_reciclaje_app", blank=True)
    information  = models.TextField()
    created_at = models.DateField( auto_now_add=True, editable=False)
    update_at = models.DateField(default=datetime.datetime.now())
    def __str__(self):
        return self.name
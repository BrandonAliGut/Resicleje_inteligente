from typing import Any
from django.db import models
from cloudinary.models import CloudinaryField
from logs.models import Log_categorias



import datetime
# Create your models here.
from django.db.models.signals import post_save

class Category(models.Model):
    name        = models.CharField(max_length=50, blank=False)
    img         = CloudinaryField("ImageCategory", blank=True)
    information = models.TextField()
    created_at  = models.DateField( auto_now_add=True, editable=False)
    updated_at   = models.DateField(default=datetime.datetime.now())
    is_active       = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
def log_catgory_funtion(sender, **kwargs):
    category = kwargs['instance']
    print(kwargs)
    if kwargs["created"] == True:
        log_catgory = Log_categorias(
            img = category.img,      
            information = category.information  , 
            created_at  =category.updated_at ,   
            description = 'was created  {} at  {} activo {}'.format(category.name, str(datetime.datetime.now()), category.is_active ),    
            updated_at  =category.created_at   ,   
            name   =  category.name   ,    
            request_method='Post',
        )
        log_catgory.save()
    if kwargs["created"] == False:
        log_catgory = Log_categorias(
        img = category.img,      
        information = category.information  , 
        created_at  =category.updated_at ,   
        description = 'was updated  {} at {} // activo={}'.format(category.name, str(datetime.datetime.now()),category.is_active  ),    
        updated_at  =category.created_at   ,   
        name   =  category.name   ,    
        request_method='Put',
        )
      
        log_catgory.save()
post_save.connect(log_catgory_funtion, sender=Category)
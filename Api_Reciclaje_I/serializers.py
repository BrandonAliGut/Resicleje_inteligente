from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import Base64ImageField

class SerializerCategoria(serializers.ModelSerializer):
    img = Base64ImageField(required= False)
    class Meta:
        model   = Category
        fields  = ['id','name','img', 'information','update_at','created_at']
        
    def update(self, instance, validated_data):
        img = validated_data.get('img')
        if img and img != "":
            instance.img        = validated_data.get('img', instance.img)
        
        instance.name           = validated_data.get('name', instance.name)
        instance.information    = validated_data.get('information', instance.information)
        instance.update_at      = validated_data.get('update_at', instance.update_at)
        instance.created_at     = validated_data.get('created_at', instance.created_at)

        instance.save()
        
        return instance
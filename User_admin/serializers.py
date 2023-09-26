from rest_framework import serializers
from .models import User_models
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class User_serializar(serializers.ModelSerializer):
    class Meta: 
        model = User_models
        fields = ('id', "email",  "name","lastname", 'password')
        extra_kwargs = {
        
            'password':{
                'write_only':True,
                
                'style': {
                    'input_type':'password'
                }
            }
            }
    def create(self,validated_data):
        
        user = User_models.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            lastname = validated_data['lastname'],
            password = validated_data['password'],
            
        )
        try:
            roll=Group.objects.get(name='Invitado')
            
        except Group.DoesNotExist:
            roll = Group.objects.create(name='Invitado')
        
        user.groups.add(roll)
       
        
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop(password)
            instance.set_password(password)
            
        return super().update(instance, validated_data)
    





class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

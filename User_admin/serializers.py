from rest_framework import serializers
from .models import User_models
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
import django.contrib.auth.password_validation as validators
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from django.core import exceptions


class User_serializar(serializers.ModelSerializer):
    class Meta: 
        model = User_models
        
        fields = ('id', "email",  "name","lastname", 'password')
        extra_kwargs = {
        
            'password':{
                'write_only':True,
                'min_length':6,
                'allow_blank':False,
                
                'style': {
                    'input_type':'password'
                }
                
            }
            }
        
    def validate(self, data):
         # here data has all the fields which have validated values
         # so we can create a User instance out of it
         user = User_models(**data)
         
         # get the password from the data
         password = data.get('password')
         
         errors = dict() 
         try:
             # validate the password and catch the exception
             validators.validate_password(password=password, user=user)
         
         # the exception raised here is different than serializers.ValidationError
         except exceptions.ValidationError as e:
             errors['password'] = list(e.messages)
         
         if errors:
             raise serializers.ValidationError(errors)
          
         return super(User_serializar, self).validate(data)
        
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


from rest_framework import serializers
from rest_framework.serializers import Serializer


class UserPasswordChangeSerializer(Serializer):
    old_password = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    confirmed_password = serializers.CharField(required=True, max_length=30)

    def validate(self, data):
        # add here additional check for password strength if needed
        if not self.context['request'].user.check_password(data.get('old_password')):
            raise serializers.ValidationError({'old_password': 'Wrong password.'})

        if data.get('confirmed_password') != data.get('password'):
            raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    @property
    def data(self):
        # just return success dictionary. you can change this to your need, but i dont think output should be user data after password change
        return {'Success': True}
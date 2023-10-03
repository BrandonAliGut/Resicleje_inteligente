from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model
from django.utils.dateformat import format
from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth import logout

from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.viewsets import GenericViewSet
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView

from .models import User_models
from .serializers import *
from .tokenpermisos import ObtainAuthToken
from .permissions import UpdateOwnProfile



# Create your views here.


class UserViewset(mixins.CreateModelMixin,GenericViewSet):
    serializer_class = User_serializar
    queryset = User_models.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        #user = serializer.validated_data['user']
        #password=serializer.validated_data['password']
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginApiView(ObtainAuthToken):
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        password=serializer.validated_data['password']
        
        
        usermodel = User_models.objects.get(pk = user.pk)
        try:
            old_token = Token.objects.get(user=usermodel) 
            if old_token:
                old_token.delete()
                token, created = Token.objects.get_or_create(user=request.user)
            else:
                token, created = Token.objects.get_or_create(user=usermodel)
                
        except:
            token, created = Token.objects.get_or_create(user=usermodel)
        
            
        user_autheticated = authenticate(request,username=user, password=password)
        if user is not None:
            login(request, user_autheticated)
        from django.core import serializers as serial
        roll=user.groups.all()
        import json
        roll_json = []
        for roll in roll:
            roll_json.append({str(roll.id):str(roll.name)})
            
        
        return Response({
            'user':  {
                'id': user.pk,
                'email':user.email,
                'name': user.name,
                'lastname':user.lastname,
                'created_at':user.created_at,
                'update_at':user.update_at,
                'roles': roll_json,
                },
            'token': token.key
            })
       
class APIChangePasswordView(UpdateAPIView):
    serializer_class = UserPasswordChangeSerializer
    model = get_user_model() # your user model
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user    
    


@api_view(['GET'])
@authentication_classes(( TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def refresh_token(request, format=None):
    user = request.user
    usermodel = User_models.objects.get(pk = user.pk)
    
    try:
        old_token = Token.objects.get(user=usermodel) 
        if old_token:
            old_token.delete()
            token, created = Token.objects.get_or_create(user=request.user)
        else:
            token, created = Token.objects.get_or_create(user=usermodel)
        
    except:
        token, created = Token.objects.get_or_create(user=usermodel)
    
    from django.core import serializers as serial
    roll=user.groups.all()
    import json
    roll_json = []
    for roll in roll:
        roll_json.append({str(roll.id):str(roll.name)})
        
    try: 
        response = {
        'user':  {
            'id': user.pk,
            'email':user.email,
            'name': user.name,
            'lastname':user.lastname,
            'created_at':user.created_at,
            'update_at':user.update_at,
            'roles': roll_json,
            },
        "new_token": token.key,
        "creation_date": str(token.created)
        }
    except: 
        response = {
         "error": "Unable to refresh key. Please try again."
        }
        
    return JsonResponse(response)




@api_view(['GET'])
@authentication_classes(( TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def logout_view(request, format=None):
    try: 
        old_token = Token.objects.get(user=request.user) 
        with transaction.atomic():
            old_token.delete()
    except Token.DoesNotExist:
        pass
    logout(request)


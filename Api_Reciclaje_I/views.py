from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
# Create your views here.
class View_category(APIView):
    
    #SessionAuthentication : permite el pase si existe una cession activa : authentication_classes = [.. , SessionAuthentication]
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        #print(request.user.get_group_permissions())
        self.check_permissions_roll(request, 'Api_Reciclaje_I.view_category' )
        
        if request.user.is_authenticated:
            content = {
                'user': str(request.user),  # `django.contrib.auth.User` instance.
                'auth': str(request.user.is_authenticated),  # None
            }
            return Response(content)
        
        
        
    def check_permissions_roll(self, request, permissionuseroll):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        if not request.user.is_admin:
            if not permissionuseroll in request.user.get_group_permissions() :
                self.permission_denied(
                    request,
                    message=getattr(permissionuseroll, 'message', None),
                    code=getattr(permissionuseroll, 'code', None)
                )
        
            
from rest_framework import viewsets
from .models import Category
from .serializers import SerializerCategoria

"class Prueva(viewsets.ModelViewSet):"
class Category_Api(APIView):
    
    #SessionAuthentication : permite el pase si existe una cession activa : authentication_classes = [.. , SessionAuthentication]

    def get(self, request, format=None):
        #self.check_permissions_roll(request, 'Api_Reciclaje_I.view_category' )
        items = Category.objects.all()
        serializer = SerializerCategoria(items, many=True)
        return Response(serializer.data)
    
    

    def post(self, request, format=None):
        
        post_data = {
            'name': request.data.get('name'),
            'img': request.data.get('img'),
            'information': request.data.get('information'),
            'update_at': request.data.get('update_at'),
            'created_at': request.data.get('created_at'),}
        
        serializer = SerializerCategoria(data=post_data)
        serializer.is_valid(raise_exception=True)
        self.check_permissions_roll(request, 'Api_Reciclaje_I.add_category' )
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def check_permissions_roll(self, request, permissionuseroll):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        if not request.user.is_admin:
            if not permissionuseroll in request.user.get_group_permissions() :
                self.permission_denied(
                    request,
                    message=getattr(permissionuseroll, 'message', None),
                    code=getattr(permissionuseroll, 'code', None)
                )
    
        
        
  
        
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.utils.decorators import method_decorator
""" 

from .models import *
from .serializers import *
# Create your views here.
# Create your views here.
@api_view(["GET", "POST"])
@method_decorator(csrf_protect)
@requires_csrf_token
def categorylist(request, format= None):
    if request.method =="GET":
        model  = Category.objects.all()
        serilzers = SerializerCategoria(model, many = True)
        return Response(serilzers.data)
    
    elif request.method == "POST":
        serializers = SerializerCategoria(data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
"""

@api_view(["GET", 'PUT', "DELETE"])
@requires_csrf_token
def categoria_detail(request, pk):
    try:
        model  = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    if request.method =='GET':
        serializers = SerializerCategoria(model)
        return Response(serializers.data)
    
    elif request.method == "PUT":
        serializers = SerializerCategoria(model, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        model.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)  
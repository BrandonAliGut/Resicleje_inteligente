from django.shortcuts import render

#importaciones para vistas basadas en funciones
from rest_framework.response import Response
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import requires_csrf_token



#Importaciones para vistas basadas en clases
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Category
from .serializers import SerializerCategoria



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
        permisos = self.check_permissions_roll(request, 'Api_Reciclaje_I.add_category' )
                
        if permisos:
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
                return False
            return False
        return True
    
        
        
  
        




@api_view(["GET", 'PUT', "DELETE"])
@permission_required("polls.add_choice")
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
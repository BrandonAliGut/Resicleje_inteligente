from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
# Create your views here.
class ExampleView(APIView):
    
    #SessionAuthentication : permite el pase si existe una cession activa : authentication_classes = [.. , SessionAuthentication]
    
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):

        #print(request.user.get_group_permissions())
        if 'Api_Reciclaje_I.view_category' in request.user.get_group_permissions():
            if request.user.is_authenticated:
                content = {
                    'user': str(request.user),  # `django.contrib.auth.User` instance.
                    'auth': str(request.user.is_authenticated),  # None
                }
                return Response(content)
        
        return Response(data = { "detail": "not esta autorizado"}, status=400)
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

"""router = DefaultRouter()
router.register('api/Category', Category_Api, 'Category')"""

urlpatterns = [
    path('api/categories', Category_Api.as_view()),
    path('api/categories/<int:pk>/', categoria_detail, name="update_del_category"), 
    
    
] 


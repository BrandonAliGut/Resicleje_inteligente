from .views import *
from django.urls import path, include


urlpatterns = [
    path("", home, name="home"),
    path("acerca", acerca_de, name="acerca_de"),
    
    
    path("category", categoryView)

]

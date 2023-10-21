from .views import *
from django.urls import path, include


urlpatterns = [
    path("", home, name="home"),
    path("acerca", acerca_de, name="acerca_de"),
    path("papel", papel, name="papel"),
    path("metales", metales, name="metales"),
    path("plastico", plastico, name="plastico"),
    path("vidrio", vidrio, name="vidrio"),
    
    path("category", categoryView)

]

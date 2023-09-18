from .views import *
from django.urls import path, include


urlpatterns = [
    path('Home/', CategoryView.as_view(), name="Home"),

]
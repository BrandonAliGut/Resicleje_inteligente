from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

router = DefaultRouter()
router.register('register', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login', UserLoginApiView.as_view()),
    path('token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('token/refresh',  refresh_token)
]
#admin

#Invitado_prueva

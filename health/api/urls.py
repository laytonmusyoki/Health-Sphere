from django.contrib import admin
from django.urls import path

from .views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signin/',login_user,name="login_user"),
    path('register/',Register_user,name="Register")
]

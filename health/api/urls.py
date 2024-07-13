from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from .views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signin/',login_user,name="login_user"),
    path('register/',Register_user,name="Register"),
    path('otp-verify/',otpVerification,name="otp-otpVerification"),
    path('password-reset/', password_reset_request, name='password-reset'),
    path('password-reset-confirm/<str:token>/', password_reset_confirm, name='password-reset-confirm'),
    
]

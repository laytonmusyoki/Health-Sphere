from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializer import *
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def Register_user(request):
    data=request.data
    serializer=Register(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status":201,"success":f"Account created for {serializer.data['username']}"})
    else:
        return Response({"status":400,
            "message":serializer.errors
            },status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login_user(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    
    if not serializer.is_valid():
        return Response({
            "status": 400,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
    
    if not user:
        return Response({
            "status": 400,
            "error": 'Invalid credentials'
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        verified=OtpCode.objects.filter(user=user,verified=True).exists()
        if not verified:
            return Response({
                "status": 400,
                "error": 'Please verify your account first'
            }, status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        return Response({
            'status': 200,
            'access': access_token,
            'refresh': refresh_token
        }, status=status.HTTP_200_OK)
    

@api_view(['POST'])
def password_reset_request(request):
    if request.method == 'POST':
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password reset link sent"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def password_reset_confirm(request, token):
    try:
        token_obj = Token.objects.get(token=token)
    except Token.DoesNotExist:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

    user = token_obj.user
    user.set_password(request.data['password'])
    user.save()
    
    # Optionally, delete the token after use
    token_obj.delete()
    
    return Response({"message": "Password has been reset"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def otpVerification(request):
    data=request.data
    otp=data['otp']
    otp_obj=OtpCode.objects.filter(otp=otp).exists()
    if otp_obj:
        otp_obj=OtpCode.objects.get(otp=otp)
        otp_obj.verified=True
        otp_obj.save()
        return Response({"message":"Account verified successfuly"},status.HTTP_200_OK)
    else:
        return Response({"message":"Invalid OTP"},status=status.HTTP_400_BAD_REQUEST)
    
from django.contrib.auth.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import ChangePasswordSerializer, MyTokenObtainPairSerializer, RegisterSerializer, UpdateUserSerializer

from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
  permission_classes = (AllowAny,)
  serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
  queryset = User.objects.all()
  permission_classes = (IsAuthenticated,)
  serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
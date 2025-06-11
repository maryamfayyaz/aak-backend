from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


class HealthCheckView(APIView):
  def get(self, request):
    return Response(status=status.HTTP_200_OK)

class LoginView(APIView):
  def post(self, request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.validated_data['user']
      refresh_token = RefreshToken.for_user(user)
      user_data = SignupSerializer(user).data

      return Response({
        "message": "Login successful",
        "refresh": str(refresh_token),
        "token": str(refresh_token.access_token),
        "user": user_data
      })

    raise serializers.ValidationError(serializer.errors)


class SignupView(APIView):
  def post(self, request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      refresh_token = RefreshToken.for_user(user)
      return Response({
        "message": "Signup successful",
        "refresh": str(refresh_token),
        "token": str(refresh_token.access_token),
        "user": SignupSerializer(user).data
      })

    raise serializers.ValidationError(serializer.errors)

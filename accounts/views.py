from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import UserSerializer, LoginSerializer

from utils.jwtTokenService import generate_token


class RegisterAPI(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"error": False, "message": "User Registered Successfully!"}, status=201
            )
        return Response({"error": True, "message": serializer.errors}, status=400)


class LoginAPI(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        try:
            user = User.objects.get(email=email)
            password_match = check_password(password, user.password)
            if password_match:
                token = generate_token(email)
                user_data = UserSerializer(user).data

                return Response(
                    {
                        "error": False,
                        "message": "User logged in successfully!",
                        "data": user_data,
                        "token": token,
                    },
                    status=200,
                )
            return Response(
                {"error": True, "message": "Password is not Matched!"},
                status=400,
            )
        except User.DoesNotExist:
            return Response(
                {"error": True, "message": "User does not exist."},
                status=404,
            )
        except Exception as e:
            return Response({"error": True, "message": str(e)}, status=400)

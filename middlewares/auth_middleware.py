from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
import jwt
from accounts.models import User


class CustomAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.path.startswith("/api/admin/")
            or request.path.startswith("/api/media/")
            or request.path.startswith("/favicon.ico")
            or request.path.startswith("/api/static/")
            or request.path.startswith("/api/schema/")
            or request.path.endswith("nt/")
        ):
            request.thisUser = None
            response = self.get_response(request)
            return response
        token = request.headers.get("x-access-token")

        if not token:
            return JsonResponse(
                {"error": True, "message": "Credentials Not Found ..Please Login"},
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            payload = jwt.decode(
                token,
                settings.JWT_KEY,
                algorithms=["HS256"],
            )
        except jwt.ExpiredSignatureError:
            return JsonResponse(
                {"error": True, "message": "Token has expired. Please login again."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except jwt.InvalidTokenError:
            return JsonResponse(
                {"error": True, "message": "Invalid token. Please login again."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        user = User.objects.filter(email=payload["email"]).first()
        request.thisUser = user
        response = self.get_response(request)
        return response

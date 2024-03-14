import datetime

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

import jwt

from .models import User
from .serializers import UserSerializer


class UserRegisterAPIView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class UserLoginAPIView(APIView):
    
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {
            "message": "Successfull login"
        }

        return response


class UserAPIView(APIView):

    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserLogoutAPIView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            "message": "Successfull logout"
        }

        return response

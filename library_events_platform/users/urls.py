from django.urls import path

from .views import UserRegisterAPIView, UserLoginAPIView, UserAPIView, UserLogoutAPIView


urlpatterns = [
    path("user/register/", UserRegisterAPIView.as_view()),
    path("user/login/", UserLoginAPIView.as_view()),
    path("user/", UserAPIView.as_view()),
    path("user/logout/", UserLogoutAPIView.as_view()),
]

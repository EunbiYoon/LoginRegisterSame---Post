from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView


urlpatterns = [
    path('login',UserLoginView, name="login"),
    path('register',UserRegisterView, name="register"),
    path('logout',UserLogoutView, name="logout"),
]


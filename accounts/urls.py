from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerUser, name="register-user"),
    # path("login/", views.loginUser, name="login-user"),
]
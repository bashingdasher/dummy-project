from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path("register/", views.registerUser, name="register-user"),
    #TODO: make a page for displaying user info and apps they can access
    # path("<str:pk>/", views.userInfo, name="user-info"),
    path("login/", views.loginUser, name="login-user"),
    path("logout/", views.userLogout, name="logout-user")
]
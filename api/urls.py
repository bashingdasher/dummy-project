from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "api"
urlpatterns = [
    path("users/", views.userList, name="user-list"),
    path("tasks/<str:pk>/", views.taskList, name="task-list"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
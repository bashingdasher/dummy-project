from django.urls import path, re_path, include
from . import views

app_name = "todolist"
urlpatterns = [
    path('', views.toDoList_Index, name='tdlindex'),

]
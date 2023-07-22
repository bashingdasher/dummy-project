from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.toDoList_Index, name='tdlindex')
]
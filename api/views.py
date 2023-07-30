from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import userSerializer, taskSerializer
from todolist.models import Task
from django.contrib.auth.models import User

@api_view(["POST", "GET"])
def userList(request, format=None):
    users = User.objects.all()
    if request.method == "GET":
        serializer = userSerializer(users, many=True)
        return Response(serializer.data)


@api_view(["POST", "GET"])
def taskList(request, pk, format=None):
    try:
        tasks = Task.objects.filter(author__username=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = taskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
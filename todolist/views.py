from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required(login_url="accounts:login-user")
def toDoList_Index(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        tasks = user.task_set.all()
        context.update({"tasks":tasks})

    if request.method == "POST":
        title = request.POST.get('task-title')
        description = request.POST.get('task-description')
        new_task = Task.objects.create(title=title, description=description, author=user)
        return redirect('tdlindex')

    return render(request, "todolist/tdl_index.html", context)

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


def registerUser(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)


    form = RegisterForm()

    context = {"form":form}

    return render(request, "accounts/registerpage.html", context)

# def loginUser(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
        
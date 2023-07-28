from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from base.views import indexPage


def registerUser(request):
    form = RegisterForm()
    # When user submits the info, it'll process it
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return redirect("/")
            
    # the login page 
    context = {"form":form}
    return render(request, "accounts/registerpage.html", context)


def loginUser(request):

    if request.user.is_authenticated:
        return HttpResponse("you are already logged in!")

    if request.method == "POST":
            user = get_object_or_404(User, username = request.POST.get('username'))
            if user.check_password(request.POST.get("password")):
                login(request, user)
                redirect("/")
            else:
                return HttpResponse("password is wrong. try logging in  again")
    return render(request, "accounts/loginpage.html")

def userLogout(request):
     if request.method == "POST":
          next = request.POST.get("next")
          logout(request)
          return redirect(next)


     return render(request, "accounts/logout-confirm.html")


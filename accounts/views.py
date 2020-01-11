from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserAccount

def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = UserAccount(username=username, password=password1)
        user.save()
        return redirect('/')
        
    else:
        return render(request, "signup.html")


def newUser(request):
    name = request.POST.get("username")
    passwd = request.POST.get("password")

    o_ref = UserAccount(username = name, password = passwd)
    o_ref.save()

    return render(request, 'index.html')

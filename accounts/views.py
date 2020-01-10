from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        print('User Created')
        return redirect('/')
        
    else:
        return render(request, "signup.html")
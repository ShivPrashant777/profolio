from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserAccount


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html")
    else:
        print("not POST")
        return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            o_ref = UserAccount(username=username, password=password1)
            o_ref.save()
            print('User Created')
            return userInfo(request)

        else:
            return render(request, "signup.html")

        
    else:
        return render(request, "signup.html")


def userInfo(request):
    return render(request, 'userinfo.html')

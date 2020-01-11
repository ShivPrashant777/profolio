from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserAccount


def login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']

        user_name = UserAccount.objects.get(username = userName)
        return render(request, 'test.html', {'user': user_name})
    
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            o_ref = UserAccount(username=username, password=password1)
            o_ref.save()
            return userInfo(request)

        else:
            return render(request, "signup.html")

        
    else:
        return render(request, "signup.html")


def userInfo(request):
    return render(request, 'userinfo.html')



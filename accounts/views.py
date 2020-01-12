from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserAccount


def login(request):
    if request.method == 'POST':
        Users = UserAccount.objects.all()
        input_password = request.POST['password']
        for user in Users:
            if input_password == user.password:
                return render(request, 'test.html', {'user': user})
            else:
                print("Invalid Credentials")
                return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if UserAccount.objects.get(username=username) == UserAccount.DoesNotExist:
                o_ref = UserAccount(username=username, password=password1)
                o_ref.save()
                print('User Created')
                return redirect("userinfo")
            else:
                print("User Already Exists")
                return render(request, "signup.html")
                

        else:
            print("Passwords don't Match")
            return render(request, "signup.html")
   
    else:
        return render(request, "signup.html")


def userInfo(request):
    return render(request, 'userinfo.html')



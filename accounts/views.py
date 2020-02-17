from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from accounts.models import UserAccount


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('../../user/')

        else:
            print("Invalid Credentials")
            return redirect(login)  
               

    else:
        return render(request, 'login.html')


def userpage(request, user):
   if request.method == 'POST':
        uploaded_file = request.FILES["document"]
        fs = UserAccount(file_user= uploaded_file)
        fs.save(uploaded_file)
        return render(request, 'user.html')  


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists() == False:
                o_ref = User.objects.create_user(username=username, password=password1)
                o_ref.save()
                u_ref = UserAccount(username=username, password=password1)
                u_ref.save() 
                print('User Created')
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                print(user)
                return redirect('../../user/')
            
            else:
                print("User Already Exists")
                return render(request, "signup.html")
        
        else:
            print("Passwords don't Match")
            return render(request, "signup.html")
   
    else:
        return render(request, "signup.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
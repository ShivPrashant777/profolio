from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import UserAccount
from accounts.views import signup, login
def logout(request):
    auth.logout(request)
    return redirect('/')


def userpage(request):
    if request.method == 'POST':
        uname = request.user.username
        uploaded_file = request.FILES["document"]
        fs = UserAccount(username= uname, file_user= uploaded_file)
        fs.save(uploaded_file)
    return render(request, 'user.html')




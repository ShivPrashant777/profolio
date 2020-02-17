from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import UserAccount
from accounts.views import signup, login


def userpage(request):
    if request.method == 'POST':
        uname = request.user.username
        uploaded_file = request.FILES["document"]
        emp = UserAccount.objects.get(username=uname)
        emp.file_user = uploaded_file
        emp.save()
        # fs = UserAccount(username= uname, file_user= uploaded_file)
        # fs.save(uploaded_file)
    return render(request, 'user.html')




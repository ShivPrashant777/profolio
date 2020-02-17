from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import UserAccount
from accounts.views import signup, login


def userpage(request):
    if request.method == 'POST':
        uname = request.user.username
        html_file = request.FILES["html_file"]
        css_file = request.FILES["css_file"]
        temp = UserAccount.objects.get(username=uname)
        temp.file_user = html_file
        temp.file_user_css = css_file
        temp.save()
    return render(request, 'user.html')




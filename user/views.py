from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage


def logout(request):
    auth.logout(request)
    return redirect('/')


def userpage(request):
    if request.method == 'POST':
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'user.html')



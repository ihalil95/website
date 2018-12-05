from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from homeworks.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/')
    else:
        return render(request, 'loginpage.html')
def loginme(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'loginok.html')
    else:
        return render(request, 'loginerror.html')
def panel(request):
    if request.user.is_authenticated:
        studentnumber = User.objects.get(username=request.user.username)
        seedb = posthomework.objects.filter(studentnumber=studentnumber).order_by('-date')
        context = {
            'godb': seedb,
        }
        return render(request, 'panel.html',context)
    else:
        return redirect('http://127.0.0.1:8000/loginpage')
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'logout.html')
    else:
        return redirect('http://127.0.0.1:8000/loginpage')
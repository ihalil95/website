from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
import datetime
tdy = datetime.datetime.today().strftime('%d-%m-%Y')
def index(request):
    getdata = homework.objects.all().order_by('-deadline')
    content = {
        'go' : getdata,
        'today': tdy
    }
    return render(request,'homeworks/index.html',content)
def homework_detail(request,url):
    memory = homework.objects.filter(id=url)
    context = {
        'readme' : memory,
               }
    return render(request,'homeworks/detail.html',context)
def handin(request,url):
    if request.user.is_authenticated:
        memory = homework.objects.filter(id=url)
        context = {
            'readme': memory,
        'today': tdy,
        }
        return render(request,'homeworks/handin.html',context)
    else:
        return redirect('http://127.0.0.1:8000/loginpage')
def send(request,url):
    hafiza = homework.objects.get(id=url)
    coursename = hafiza.lecture
    workname = hafiza.homeworkname
    studentnumber = User.objects.get(username=request.user.username)
    try:
        files = request.FILES['myfile']
        save = posthomework(studentnumber=studentnumber, files=files, coursename=coursename, workname=workname)
        save.save()
        return render(request, 'homeworks/send.html')
    except:
        return render(request,'homeworks/sendfail.html')


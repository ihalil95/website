from django.shortcuts import render
from .models import *
def index(request):
    getdata = teaching.objects.all()
    content = {
        'go' : getdata
    }
    return render(request,'teaching.html',content)

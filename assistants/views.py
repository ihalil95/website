from django.shortcuts import render
from .models import *
def index(request):
    getdata = assists.objects.all()
    content = {
        'read' : getdata
    }
    return render(request,'assistants.html',content)

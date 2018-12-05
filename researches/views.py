from django.shortcuts import render
from .models import *
def researchindex(request):
    getdata = researches.objects.all().order_by('-date')
    context = {
        'go' : getdata,
    }
    return render(request, 'researches/index.html', context)
def researchdetail(request,url):
    getdata = researches.objects.filter(id=url)
    context = {
        'readme' : getdata,
    }
    return render(request, 'researches/detail.html', context)
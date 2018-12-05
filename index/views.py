from django.shortcuts import render
from index.models import announcement
def homepage(request):
    getdb = announcement.objects.all()
    context = {
        'read' : getdb,
    }
    return render(request,'index.html',context)

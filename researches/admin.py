from django.contrib import admin
from .models import *

class researchclass(admin.ModelAdmin):
    list_display = ['title','keywords','keypublication']
    list_filter = ['title','keywords','keypublication']
    search_fields = ['title','keywords','keypublication']

    class Meta:
        model = researches
admin.site.register(researches,researchclass)

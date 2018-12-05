from django.contrib import admin
from .models import *
class teachingclass(admin.ModelAdmin):
    list_display = ['title','lecture']
    list_filter = ['title','lecture']
    search_fields = ['title','lecture']
    class Meta:
        model = teaching
admin.site.register(teaching,teachingclass)

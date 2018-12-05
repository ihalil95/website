from django.contrib import admin
from .models import *
class announcementclass(admin.ModelAdmin):
    list_display = ['content']

    class Meta:
        model = announcement
admin.site.register(announcement,announcementclass)
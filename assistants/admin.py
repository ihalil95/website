from django.contrib import admin
from .models import *
class assistsclass(admin.ModelAdmin):
    list_display = ['name','duty']

    class Meta:
        model = assists
admin.site.register(assists,assistsclass)

from django.contrib import admin
from .models import *
class homeworkclass(admin.ModelAdmin):
    list_display = ['homeworkname','givendate','deadline']
    list_filter = ['homeworkname','givendate','deadline']
    search_fields = ['homeworkname','givendate','deadline']
    class Meta:
        model = homework
admin.site.register(homework,homeworkclass)

class posthomeworkclass(admin.ModelAdmin):
    list_display = ['studentnumber','coursename','workname','date','files','grade']
    list_filter = ['studentnumber','coursename','workname','date','files','grade']
    search_fields = ['studentnumber','coursename','workname','date','files','grade']
    list_editable = ['grade']
    class Meta:
        model = posthomework
admin.site.register(posthomework,posthomeworkclass)
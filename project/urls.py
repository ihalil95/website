from django.contrib import admin
from django.urls import path,include
from index.views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('canttouchthis/', admin.site.urls),
    path('', homepage),
    path('publications/',include('publications.urls')),
    path('assistants/',include('assistants.urls')),
    path('researches/',include('researches.urls')),
    path('teaching/',include('teaching.urls')),
    path('homeworks/',include('homeworks.urls')),
    path('loginpage/',loginpage),
    path('login/',loginme),
    path('panel',panel),
    path('logout',logout_page),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "Site yönetimi"
admin.site.site_title = "Yönetici paneli"

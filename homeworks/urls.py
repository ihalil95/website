from django.urls import path
from .views import *
urlpatterns = [
    path('',index),
    path('detail/<int:url>',homework_detail),
    path('handin/<int:url>',handin),
    path('send/<int:url>',send),
]
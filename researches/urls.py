from django.urls import path
from .views import *
urlpatterns = [
    path('',researchindex),
    path('<int:url>',researchdetail)
]
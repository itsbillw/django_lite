"""Defines url patterns for csv_compare."""
from django.urls import path

from . import views

app_name = 'csv_compare'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path('new/', views.compare, name='compare'),
    path('example/', views.example, name='example'),
]
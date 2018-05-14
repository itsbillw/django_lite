from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('compare/', include('csv_compare.urls')),
    path('learn/', include('learning_logs.urls')),
    path('users/', include('users.urls')),
    path('', views.index, name='index'),
]
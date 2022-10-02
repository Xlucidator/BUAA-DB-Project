from http.client import ImproperConnectionState

from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'backend'

urlpatterns = [
    path('index/', views.index),
    path('index/POST/login', views.login),
    path('index/POST/enroll',views.enroll),


]

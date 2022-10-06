from http.client import ImproperConnectionState
from django.template.defaulttags import url
from django.urls import path, include
from . import views

app_name = 'backend'

urlpatterns = [
    path('login/', views.index),
    path('login/login', views.login),
    path('login/enroll', views.enroll),
]

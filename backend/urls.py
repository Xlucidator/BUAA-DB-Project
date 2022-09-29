from http.client import ImproperConnectionState
from django.urls import path
#test for git
from . import views

app_name = 'backend'

urlpatterns = [
    path('account/', views.account_manage, name='account'),
]
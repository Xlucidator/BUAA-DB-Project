from http.client import ImproperConnectionState
from django.template.defaulttags import url
from django.urls import path, include, re_path
from . import views

# data_msg的规范化
# 一些函数处理的鲁棒性
# 修改待审批队列
app_name = 'backend'

urlpatterns = [
    path('user/', views.index),  # 测试用，和前端无关
    path('login/', views.log),

    path('login/<str:module>/', views.loginView.as_view()),  # 登录界面的登录功能

    path('test/<str:CodeName>/', views.testView.as_view()),

    path('index/user/@self/', views.SelfView.as_view()),
    path('index/user/<str:CodeName>/', views.UserDetailView.as_view()),
    path('index/user/', views.UserListView.as_view()),

    path('index/application/<str:CodeName>/@accept/', views.ApplicationOtherView.as_view()),
    path('index/application/', views.ApplicationModelView.as_view({'get': 'list', 'post': 'create'})),
    path('index/application/<str:CodeName>/',
         views.ApplicationModelView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('index/profile/<str:CodeName>/', views.ProfileDetailView.as_view()),
    path('index/profile/', views.ProfileListView.as_view()),

    path('passage/passage/<str:PId>/', views.PassageDetailView.as_view()),
    path('passage/passages/<str:idx>/', views.PassageListView.as_view()),
    path('passage/passages/', views.PassageListView.as_view()),
]

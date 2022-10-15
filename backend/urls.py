from http.client import ImproperConnectionState
from django.template.defaulttags import url
from django.urls import path, include
from . import views

# data_msg的规范化
# 一些函数处理的鲁棒性
# 修改待审批队列
app_name = 'backend'

urlpatterns = [
    path('user/', views.index),  # 测试用，和前端无关
    path('login/', views.log),

    path('login/login', views.login),  # 登录界面的登录功能
    path('login/enroll', views.enroll),  # 登录界面的注册功能

    path('index/user/GET/users', views.users_get),  # 用户界面，获取所有用户信息
    path('index/user/GET/user', views.user_get),  # 用户界面，当前用户信息
    path('index/user/PUT/user', views.user_modify),  # 修改用户属性
    path('index/user/DELETE/user', views.user_delete),  # 删除用户

    path('index/application/reject', views.application_reject),  # 拒绝用户的注册申请
    path('index/application/consent', views.application_consent),  # 同意用户的注册申请
    path('index/application/GET', views.applications_get),  # 用户界面，获取所有待申请信息
    path('index/application/PUT/application', views.application_modify),  # 待申请列表的修改

]

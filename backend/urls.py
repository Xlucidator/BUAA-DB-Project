from http.client import ImproperConnectionState
from django.template.defaulttags import url
from django.urls import path, include
from . import views

app_name = 'backend'

urlpatterns = [
    path('user/', views.index),  # 测试用，和前端无关
    path('login/', views.log),

    path('login/login', views.login),  # 登录界面的登录功能
    path('login/enroll', views.enroll),  # 登录界面的注册功能
    # GET：查询，POST：新增，PUT：更新，DELETE：删除
    # 这里可以使用include语句来是表达更加整洁，但先不管啦
    path('index/user/GET/users', views.users_get),  # 用户界面，获取所有用户信息
    path('index/user/GET/user', views.user_get),  # 用户界面，当前用户信息
    path('index/user/PUT/user', views.user_modify),  # 修改用户属性
    path('index/user/DELETE/user', views.user_delete),  # 删除用户


    path('index/application/reject', views.reject_application),  # 拒绝用户的注册申请
    path('index/application/consent', views.consent_application),  # 同意用户的注册申请

    path('index/user/GET/users', views.users_get),  # 用户界面，获取所有用户信息

]

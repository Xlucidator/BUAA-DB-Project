from http.client import ImproperConnectionState
from django.template.defaulttags import url
from django.urls import path, include
from . import views

app_name = 'backend'

urlpatterns = [
    path('user/', views.index),  # 测试用，和前端无关
    path('login/',views.log),

    path('login/login', views.login),  # 登录界面的登录功能
    path('login/enroll', views.enroll),  # 登录界面的注册功能
    # GET：查询，POST：新增，PUT：更新，DELETE：删除
    # 这里可以使用include语句来是表达更加整洁，但先不管啦
    path('user/GET/users', views.user_get),  # 用户界面，获取所有用户信息
    path('user/POST/users', views.User.get),  # 新增用户
    path('user/PUT/users', views.User.get),  # 修改用户属性
    path('user/DELETE/users', views.User.get),  # 删除用户
    path('user/approve/GET/users', views.enroll),  # 功能同上，只不过是对于申请列表的操作，故不再赘述
    path('user/approve/POST/users', views.enroll),
    path('user/approve/PUT/users', views.enroll),
    path('user/approve/DELETE/users', views.enroll),
]

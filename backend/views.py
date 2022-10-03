from datetime import datetime, timedelta

import jwt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection

from rest_framework_jwt.settings import api_settings


# Create your views here.
def account_manage(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from levelsrc_req')
        list = cursor.fetchall()
        context = {'list': list}
    return render(request, "testbackend.html", context)


def check_user(username, password):
    with connection.cursor() as cursor:
        sql = 'select * from user_account where CodeName = \'' + username + "\'"

        try:
            cursor.execute(sql)
            one = cursor.fetchone()
            print(one)
            result = (one[1] == password)
            print(result)
        except:
            print('flase')
            return False

    return result


def get_jwt(username, role_data='default'):
    # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 生payload部分的方法
    # payload = jwt_payload_handler(user)  # 生成payload, 得到字典
    # encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 生成jwt的方法
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=3600),  # 单位秒
        'iat': datetime.utcnow(),
        'data': {'username': username, 'role_data': role_data}
    }
    token = jwt_encode_handler(payload)  # 生成jwt字符串

    return str(token)


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    # print(username, password)
    result = check_user(username, password)
    if result:
        date_msg = "success!"
        date_flag = "yes"
        token = get_jwt(username)
        date = {'flag': date_flag, 'msg': date_msg, 'token': token}
        return JsonResponse({'request': date})
    else:
        date_msg = "the code is wrong"
        date_flag = "no"
        date = {'flag': date_flag, 'msg': date_msg}
        return JsonResponse({'request': date})


def add_person(username, password, permission):
    with connection.cursor() as cursor:
        sql = "insert into user_account values('{}','{}','{}')".format(username, password, permission)
        print(sql)
        try:
            cursor.execute(sql)
            print("success!")
            return True
        except:
            print('False')
            return False


def enroll(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    permission = 2  # 普通干员权限为2
    result = add_person(username, password, permission)
    if result:
        date_msg = "success!"
        date_flag = "yes"
    else:
        date_msg = "enroll failed"
        date_flag = "no"
    date = {'flag': date_flag, 'msg': date_msg}
    return JsonResponse({'request': date})
    pass


def index(request):
    return render(request, 'testbackend.html')

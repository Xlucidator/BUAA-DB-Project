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
            print('false')
            return False

    return result


def login(request):
    # {'exp': xxx, 'email': '', 'user_id': 1, 'username': 'admin'}
    # user：登录的用户对象

    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username, password)
    result = check_user(username, password)
    if result:

        date_msg = "success!"
        date_flag = "yes"

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

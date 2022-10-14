from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

from backend.tools import get_jwt, check_user


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


def del_person(username, password):
    with connection.cursor() as cursor:
        sql = "delete from user_account where CodeName = '{}' and PassWord = '{}'".format(username, password)
        print(sql)
        try:
            cursor.execute(sql)
            print("success!")
            return True
        except:
            print('False')
            return False


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    # print(username, password)
    result, username, perm = check_user(username, password)
    if result:
        date_msg = "success!"
        date_flag = "yes"
        token = get_jwt(username)
        date = {'flag': date_flag, 'msg': date_msg, 'username': username, 'permission': perm, 'token':token}
        return JsonResponse({'request': date})
    else:
        date_msg = "the code is wrong"
        date_flag = "no"
        date = {'flag': date_flag, 'msg': date_msg}
        return JsonResponse({'request': date})


def enroll(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    pwConfirm = request.POST.get("pwConfirm")
    if pwConfirm != password:
        date_msg = "passwords do not coordinate"
        date_flag = "no"
    else:
        permission = 2  # 普通干员权限为2
        token = ''
        result = add_person(username, password, permission)
        if result:
            date_msg = "success!"
            date_flag = "yes"
        else:
            date_msg = "enroll failed"
            date_flag = "no"
    date = {'flag': date_flag, 'msg': date_msg}
    return JsonResponse({'request': date})

def index(request):
    return render(request, 'testbackend.html')

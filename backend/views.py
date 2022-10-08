from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

from backend.tools import get_jwt, check_user, judge


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
    result, username, perm = check_user(username, password)
    if result:
        date_msg = "success!"
        date_flag = "yes"
        token = get_jwt(username)
        judge(token)
        date = {'flag': date_flag, 'msg': date_msg, 'username': username, 'permission': perm, 'token': token}
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


def log(request):
    return render(request, 'login.html')


class User:
    def get(self, request):
        print(123)

    def post(self, request):
        print(123)

    def delete(self, request):
        print(123)

    def put(self, request):
        print(123)


def user_get(request):
    token = request.POST.get("token")
    judge(token, 1)
    # with connection.cursor() as cursor:
    #   sql = 'select * from user_account'

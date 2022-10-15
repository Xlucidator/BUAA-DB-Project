from datetime import datetime, timedelta
import jwt
from django.db import connection
from django.http import JsonResponse

JWT_SECRET_KEY = "123"
SUCCESS_DATA = {'flag': 'yes', 'msg': 'success!'}
FAIL_DATA = {'flag': 'no', 'msg': 'fail'}
NOT_ALLOWED_DATA = {'flag': 'no', 'msg': 'not allowed'}


def get_jwt(username, role_data='default'):
    # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 生payload部分的方法
    # payload = jwt_payload_handler(user)  # 生成payload, 得到字典
    #
    # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 生成jwt的方法
    # print(jwt.decode(token,JWT_SECRET_KEY))
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=3600),  # 单位秒
        'iat': datetime.utcnow(),
        'data': {'username': username, 'role_data': role_data}
    }

    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    print(token)
    print(jwt.decode(token, JWT_SECRET_KEY))
    return str(token)


def check_user(username, password):
    with connection.cursor() as cursor:
        sql = 'select * from user_account where CodeName = \'' + username + "\'"
        try:
            cursor.execute(sql)
            one = cursor.fetchone()
            result = (one[1] == password)
        except:
            print('false')
            return False
    return result


def judge(token, std):
    test = str.encode(token)[2:-1]
    # 前端返回的字符串的格式？
    # 这里不是很确定，调试的时候再说
    try:
        result = jwt.decode(test, JWT_SECRET_KEY, algorithms='HS256', options={"verify_signature": False})
        name = result['data']['username']
        print(name)
        with connection.cursor() as cursor:
            sql = 'select * from user_account where CodeName = \'' + name + "\'"
            cursor.execute(sql)
            one = cursor.fetchone()
            return one[2] <= std
    except:
        return False


def token2name(token):
    test = str.encode(token)[2:-1]
    result = jwt.decode(test, JWT_SECRET_KEY, algorithms='HS256', options={"verify_signature": False})
    return result['data']['username']


def all_users():
    sql = 'select * from user_account'
    with connection.cursor() as cursor:
        cursor.execute(sql)
        dict_list = []
        for item in cursor:
            # CodeName | Password | Permission
            dict_list.append({'CodeName': item[0], 'Permission': item[2]})
    return dict_list


def modify_user(name, permission):
    try:
        sql = "update user_account Set Permission = " + permission + "where CodeName = \''" + name + "\'"
        with connection.cursor() as cursor:
            cursor.execute(sql)
        return JsonResponse({'request': SUCCESS_DATA})
    except:
        return JsonResponse({'request': FAIL_DATA})


def delete_user(name):
    try:
        sql = "delete from user_account where CodeName = \''" + name + "\'"
        with connection.cursor() as cursor:
            cursor.execute(sql)
        return JsonResponse({'request': SUCCESS_DATA})
    except:
        return JsonResponse({'request': FAIL_DATA})


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


def reject(name):
    try:
        with connection.cursor() as cursor:
            sql = "delete from account_approve_queue where CodeName = '{}' ".format(name)
            cursor.execute(sql)
            return JsonResponse({'request': SUCCESS_DATA})
    except:
        return JsonResponse({'request': FAIL_DATA})


def consent(CodeName, Permission):
    print(CodeName)
    try:
        with connection.cursor() as cursor:
            sql1 = "select * from account_approve_queue where CodeName = '{}' ".format(CodeName)
            print(sql1)

            cursor.execute(sql1)
            one = cursor.fetchone()
            print(one)
            CodeName = one[0]
            Class = one[1]
            region = one[2]
            Race = one[3]
            Description = one[4]
            Password = one[5]

            sql2 = "insert into user_account values('{}','{}',{},'{}','{}','{}','{}','{}')".format(CodeName, Password,
                                                                                                   Permission,
                                                                                                   "", region, Race, "",
                                                                                                   "", "")
            print(sql2)
            cursor.execute(sql2)
            sql3 = "delete from account_approve_queue where CodeName = '{}' ".format(CodeName)
            print(sql3)
            cursor.execute(sql3)
            return JsonResponse({'request': SUCCESS_DATA})
    except:
        return JsonResponse({'request': FAIL_DATA})


def one_user(token):
    try:
        name = token2name(token)
        print(name)
        with connection.cursor() as cursor:
            sql = 'select * from user_account where CodeName = \'' + name + "\'"
            cursor.execute(sql)
            one = cursor.fetchone()
            data = {'CodeName': one[0], 'token': token}
            return JsonResponse({'request': SUCCESS_DATA, 'result': data})
    except:
        return JsonResponse({'request': FAIL_DATA})


def add_into_queue(CodeName, Class, Region, Race, Description, Password):
    try:
        with connection.cursor() as cursor:
            sql = "insert into account_approve_queue values('{}','{}','{}','{}','{}','{}')".format(CodeName, Class,
                                                                                                   Region, Race,
                                                                                                   Description,
                                                                                                   Password)
            print(sql)
            cursor.execute(sql)
        return JsonResponse({'request': SUCCESS_DATA})
    except:
        return JsonResponse({'request': FAIL_DATA})


def all_applications():
    sql = 'select * from account_approve_queue'
    with connection.cursor() as cursor:
        cursor.execute(sql)
        dict_list = []
        for item in cursor:
            # CodeName | Class | Region | Race | Description
            # CodeName | Password | Permission
            dict_list.append(
                {'CodeName': item[0], 'Class': item[1], 'Region': item[2], 'Race': item[3], 'Description': item[4]})
        return dict_list

from django.shortcuts import render
from django.http import JsonResponse
from backend.tools import get_jwt, check_user, judge, all_users, modify_user, delete_user, add_person, consent, reject, \
    one_user

SUCCESS_DATA = {'flag': 'yes', 'msg': 'success!'}
FAIL_DATA = {'flag': 'no', 'msg': 'fail'}
NOT_ALLOWED_DATA = {'flag': 'no', 'msg': 'not allowed'}


# 代码重复度太高了，应该去寻找一些方法进行替换

def login(request):
    code_name = request.POST.get("CodeName")
    password = request.POST.get("PassWord")
    result = check_user(code_name, password)
    if result:
        token = get_jwt(code_name)
        d = {'CodeName': code_name, 'token': token}
        return JsonResponse({'request': SUCCESS_DATA, 'result': d})
    else:
        return JsonResponse({'request': FAIL_DATA})


def enroll(request):
    code_name = request.POST.get("CodeName")
    password = request.POST.get("password")
    pwConfirm = request.POST.get("pwConfirm")
    if pwConfirm != password:
        return JsonResponse({'request': FAIL_DATA})
    else:
        permission = 2  # 普通干员权限为2
        result = add_person(code_name, password, permission)
        if result:
            return JsonResponse({'request': SUCCESS_DATA})
        else:
            return JsonResponse({'request': FAIL_DATA})

def users_get(request):
    token = request.POST.get("token")
    allowance = judge(token, 1)
    print(allowance)
    if allowance:
        return JsonResponse({'request': SUCCESS_DATA, 'result': all_users()})
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


def user_get(request):
    token = request.POST.get("token")
    return one_user(token)


def user_modify(request):
    token = request.POST.get("token")
    code_name = request.POST.get("CodeName")
    permission = request.POST.get("Permission")
    allowance = judge(token, 1)
    if allowance:
        return modify_user(code_name, permission)
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


def user_delete(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    allowance = judge(token, 1)
    if allowance:
        return delete_user(name)
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


def reject_application(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    allowance = judge(token, 1)
    if allowance:
        return reject(name)
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


def consent_application(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    allowance = judge(token, 1)
    if allowance:
        return consent(name)
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


# 后端调试使用
def index(request):
    return render(request, 'testbackend.html')


def log(request):
    return render(request, 'login.html')

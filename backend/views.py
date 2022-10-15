from django.shortcuts import render
from django.http import JsonResponse
from backend.tools import get_jwt, check_user, judge, all_users, modify_user, delete_user, add_person, consent, reject, \
    one_user, add_into_queue, all_applications, modify_application

SUCCESS_DATA = {'flag': 'yes', 'msg': 'success!'}
FAIL_DATA = {'flag': 'no', 'msg': 'fail'}
NOT_ALLOWED_DATA = {'flag': 'no', 'msg': 'not allowed'}


# 代码重复度太高了，应该去寻找一些方法进行替换

def login(request):
    CodeName = request.POST.get("CodeName")
    Password = request.POST.get("Password")
    result = check_user(CodeName, Password)
    print(result)
    if result:
        token = get_jwt(CodeName)
        d = {'CodeName': CodeName, 'token': token}
        return JsonResponse({'request': SUCCESS_DATA, 'result': d})
    else:
        return JsonResponse({'request': FAIL_DATA})


def enroll(request):
    CodeName = request.POST.get("CodeName")
    Class = request.POST.get("Class")
    Region = request.POST.get("Region")
    Race = request.POST.get("Race")
    Description = request.POST.get("Description")
    Password = request.POST.get("Password")
    print("test1\n")
    return add_into_queue(CodeName, Class, Region, Race, Description, Password)


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


def application_reject(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    allowance = judge(token, 1)
    if allowance:
        return reject(name)
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


def application_consent(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    Permission = request.POST.get("Permission")
    allowance = judge(token, 1)
    if allowance:
        return consent(name, Permission)
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


def applications_get(request):
    token = request.POST.get("token")
    allowance = judge(token, 1)
    if allowance:
        return JsonResponse({'request': SUCCESS_DATA, 'result': all_applications()})
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})


# 后端调试使用
def index(request):
    return render(request, 'testbackend.html')


def log(request):
    return render(request, 'login.html')


def application_modify(request):
    token = request.POST.get("token")
    Permission = request.POST.get("Permission")
    CodeName = request.POST.get("CodeName")
    Class = request.POST.get("Class")
    Region = request.POST.get("Region")
    Race = request.POST.get("Race")
    Description = request.POST.get("Description")
    allowance = judge(token, 1)
    if allowance:
        return modify_application(CodeName, Permission, Class, Region, Race, Description)
    else:
        return JsonResponse({'request': NOT_ALLOWED_DATA})

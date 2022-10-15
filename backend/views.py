from django.shortcuts import render
from django.http import JsonResponse
from backend.tools import get_jwt, check_user, judge, all_users, modify_user, delete_user, add_person, consent, reject, \
    one_user, add_into_queue, all_applications, modify_application, success, fail


def login(request):
    CodeName = request.POST.get("CodeName")
    Password = request.POST.get("Password")
    return check_user(CodeName, Password)



def enroll(request):
    CodeName = request.POST.get("CodeName")
    Class = request.POST.get("Class")
    Region = request.POST.get("Region")
    Race = request.POST.get("Race")
    Description = request.POST.get("Description")
    Password = request.POST.get("Password")
    return add_into_queue(CodeName, Class, Region, Race, Description, Password)


def users_get(request):
    token = request.POST.get("token")
    allowance = judge(token, 1)
    if allowance:
        return success('成功', all_users())
    else:
        return fail('无访问权限')


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
        return fail('无访问权限')


def user_delete(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    allowance = judge(token, 1)
    if allowance:
        return delete_user(name)
    else:
        return fail('无访问权限')


def application_reject(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    allowance = judge(token, 1)
    if allowance:
        return reject(name)
    else:
        return fail('无访问权限')


def application_consent(request):
    token = request.POST.get("token")
    name = request.POST.get("CodeName")
    Permission = request.POST.get("Permission")
    allowance = judge(token, 1)
    if allowance:
        return consent(name, Permission)
    else:
        return fail('无访问权限')


def applications_get(request):
    token = request.POST.get("token")
    allowance = judge(token, 1)
    if allowance:
        return success('成功获取', all_applications())
    else:
        return fail('无访问权限')


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
        return JsonResponse({'request': fail('无访问权限')})

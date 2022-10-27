from django.shortcuts import render
from backend.tools import get_jwt, check_user, judge, all_users, modify_user, delete_user, consent, reject, \
    one_user, add_into_queue, all_applications, modify_application, success, fail

user_account = ['CodeName', 'Password', 'Permission', 'Class', 'Region', 'Race', 'Avatar', 'Mail']
account_approve_queue = ['CodeName', 'Password', 'Permission', 'Class', 'Region', 'Race', 'Description']


# 登录页面对应接口
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


# 用户表对应接口
def users_get(request):
    token = request.POST.get("token")
    allowance = judge(token, 1)
    if allowance:
        return success('所有用户信息获取成功', all_users())
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


# 请求队列对应接口
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
    allowance = judge(token, 1)
    print("application_consent", name)
    if allowance:
        return consent(name)
    else:
        return fail('无访问权限')


def applications_get(request):
    token = request.POST.get("token")
    allowance = judge(token, 1)
    if allowance:
        return success('所用待审批列表获取成功', all_applications())
    else:
        return fail('无访问权限')


def application_modify(request):
    token = request.POST.get("token")
    CodeName = request.POST.get(account_approve_queue[0])
    Password = request.POST.get(account_approve_queue[1])
    Permission = request.POST.get(account_approve_queue[2])
    Class = request.POST.get(account_approve_queue[3])
    Region = request.POST.get(account_approve_queue[4])
    Race = request.POST.get(account_approve_queue[5])
    Description = request.POST.get(account_approve_queue[6])
    allowance = judge(token, 1)
    if allowance:
        return modify_application(CodeName, Permission, Class, Region, Race, Description)
    else:
        return fail('无访问权限')


# 后端调试使用
def index(request):
    return render(request, 'testbackend.html')


def log(request):
    return render(request, 'login.html')

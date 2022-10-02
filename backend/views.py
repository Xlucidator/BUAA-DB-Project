from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection

# Create your views here.
# def account_manage(request):
#     with connection.cursor() as cursor:
#         cursor.execute('select * from levelsrc_req')
#         list = cursor.fetchall()
#         context = {'list': list}
#     return render(request, "testbackend.html", context)


def check_user(username, password):
    # db = pymysql.connect(host='127.0.0.1', user='root', password='88014363', port=3306, db='project')
    # tt = db.cursor()
    sql = 'select * from user_account where CodeName = ' + username
    
    with connection.cursor() as cursor:
        print("im in")
        cursor.execute(sql)  # 查询到条数
        one = cursor.fetchone()  # 获得第一条数据
        print(one[0], one[1])
        result = (one[1] == password)
    print(result)
    return result


def login(request):
    # text = request.POST.get("q")
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username, password)
    result = check_user(username, password)
    if result:
        data_msg = "登陆成功"
        data_flag = "yes"
        print("成功")
    else:
        data_msg = "密码输入错误"
        data_flag = "no"
    data = {'flag': data_flag, 'msg': data_msg}
    return JsonResponse({'request': data})


def index(request):
    return render(request, 'testbackend.html')

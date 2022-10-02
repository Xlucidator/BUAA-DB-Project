from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
import pymysql


# Create your views here.
def account_manage(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from levelsrc_req')
        list = cursor.fetchall()
        context = {'list': list}
    return render(request, "testbackend.html", context)


def check_user(username, password):
    db = pymysql.connect(host='127.0.0.1', user='root', password='88014363', port=3306, db='project')
    tt = db.cursor()
    sql = 'select * from user where username = ' + username
    try:
        tt.execute(sql)  # 查询到条数
        one = tt.fetchone()  # 获得第一条数据
        result = (one[1] == password)

    except:
        print('查收数据失败')
        result = False

    tt.close()  # 关闭游标的使用
    db.close()
    print(result)
    return result


def login(request):
    text = request.POST.get("q")
    username = request.POST.get("username")
    password = request.POST.get("password")
    result = check_user(username, password)
    if result:
        date_msg = "登陆成功"
        date_flag = "yes"
        print("成功")
    else:
        date_msg = "密码输入错误"
        date_flag = "no"
    date = {'flag': date_flag, 'msg': date_msg}
    return JsonResponse({'request': date})


def index(request):
    return render(request, 'testbackend.html')

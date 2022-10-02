from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def account_manage(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from levelsrc_req')
        list = cursor.fetchall()
        context = {'list': list}
    return render(request, "testbackend.html", context)
from django.shortcuts import render
from django.http import HttpResponse
from .admin import BookInfo

# Create your views here.

def index(request):
    print("请求",request)
    return HttpResponse("首页")

def list(request):
    print("请求",request)
    return HttpResponse("列表页")

def detail(request,id):
    try:
        book = BookInfo.objects.get(pk=int(id))
        return HttpResponse(book)
        # return HttpResponse("详情页"+str(id))
    except:
        return HttpResponse("请输入正确id")
"""
视图函数
将函数和路由绑定
"""




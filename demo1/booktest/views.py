from django.shortcuts import render
from django.http import HttpResponse
from .admin import BookInfo
from django.template import loader
# Create your views here.
# 定义视图函数
def index(request):
#     print("请求",request)
#     return HttpResponse("首页")
#     加载模板（html页面）
#     template = loader.get_template('booktest/index.html')
    # 构造上下文（username 与html页面内容联系 ）
    # context = {"username":'wlh'}
    # 渲染模板
    # result = template.render(context=context)
    # 返回模板
    # return HttpResponse(result)

    return render(request,'booktest/index.html',{"username":"wlh"})

def list(request):
    print("请求",request)
    # BookInfo.objects.all() 查询BookInfo内的所有信息
    b1 = BookInfo.objects.all()
    return render(request,'booktest/list.html',context={'booklist':b1})

def detail(request,id):
    # try:
    #     book = BookInfo.objects.get(pk=id)
    #     return HttpResponse(book)
    #     # return HttpResponse("详情页"+str(id))
    # except:
    #     return HttpResponse("请输入正确id")

    book = BookInfo.objects.get(pk=id)
    # return render(request, 'booktest/detail.html', {'book': book})
    return render(request, 'booktest/detail.html', context={'book': book})
    # return HttpResponse("请输入正确id")
"""
视图函数
将函数和路由绑定
"""


"""
html页面就是模板
创建模板文件夹 templates
配置模板目录  在os.path.join(BASE_DIR,'templates')
创建项目模板目录，创建模板

加载模板 temp=loader.get_template()
使用变量渲染模板 result = temp.render({})
返回  HttpResponse(result)
"""



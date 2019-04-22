from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .admin import BookInfo, HeroInfo
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

    return render(request,'booktest/index.html',{"username": "wlh"})

def list(request):
    print("请求",request)
    # BookInfo.objects.all() 查询BookInfo内的所有信息
    b1 = BookInfo.objects.all()
    return render(request, 'booktest/list.html', context={'booklist':b1})

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

def delete(request,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        b1 = BookInfo.objects.all()
        # 使用render没有刷新请求url
        # return render(request, 'booktest/list.html', {'booklist':b1})
        # 重定向     重新向服务器发起请求 刷新url

        # return HttpResponseRedirect('/list/', {"booklist": b1})
        # 视图中解除硬编码 用 reverse
        # return HttpResponseRedirect(reverse('booktest:list'))
        # redirect是HttpResponseRedirect的简写
        return redirect(reverse('booktest:list'))

    except:
        return HttpResponse("删除失败")

def addHero(request,bookid):
        return render(request, 'booktest/addHero.html', {'bookid': bookid})


# 添加英雄信息进数据库
def addherohandler(request):
    bookid = request.POST['bookid']
    hname = request.POST['heroname']
    hgender = request.POST['sex']
    hconnect = request.POST['herocontent']

    book = BookInfo.objects.get(pk=bookid)

    hero = HeroInfo()
    hero.hname = hname
    hero.hgender = True
    hero.hcontent = hconnect
    hero.hbook = book
    hero.save()

    return HttpResponseRedirect('/detail/'+str(bookid)+'/', {'book': book})
    # return HttpResponse('添加成功')



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



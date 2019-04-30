from django.shortcuts import render,redirect,reverse,HttpResponseRedirect,HttpResponse
from .models import UserInfo,BookInfo,BorrowInfo,HotPic,MessageInfo
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,BadSignature,SignatureExpired

from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
# Create your views here.

def index(request):
    """首页"""
    hotpics = HotPic.objects.all().order_by('index')
    messageinfos = MessageInfo.objects.all()
    return render(request, 'index.html', {'hotpics': hotpics, 'messageinfos': messageinfos})

"""
#1.得到序列化工具，构造序列化对象
# 生成秘钥，加密方式有效时间300秒
serutil = Serializer(settings.SECRET_KEY, 300)
# 加密字段为userid对应的值101
result = serutil.dumps({'userid':101}).decode('utf-8')
print(result)
send_mail("点击激活账户", " <a href = 'http://127.0.0.1:8000/booklibrary/active/%s'> 点击我激活账户</a> "%(resultid,),settings.DEFAULT_FROM_EMAIL,[email])

# 2.反序列化对象
deser = Serializer(settings.SECRT_KEY,300)
try:
    obj = deser.loads(idstr)
    user = UserInfo.objects.get(pk=obj['userid'])
    user.is_active = True
    user.save()
    return redirect(reverse('booklibrary:readerlogin'))

except SignatureExpired as e:
    return HttpResponse("连接失效")
"""


def edit(request):
    """注册"""
    if request.method == "GET":
        return render(request, 'edit.html')
    elif request.method == "POST":
        title = request.POST['title']
        message = request.POST['message']
        # 将接收的信息存进数据库
        messageinfo = MessageInfo(title=title, message=message)
        # 将接收的信息存进数据库
        # messageinfo = MessageInfo()
        # messageinfo.title = title
        # messageinfo.message = message
        messageinfo.save()
        return redirect(reverse('booktest:index'))

def sendemail(request):
    """发送文件"""
    try:
        from django.conf import settings
        send_mail("Django邮件0", "Django可以发送邮件", settings.DEFAULT_FROM_EMAIL, ["2430756697@qq.com", "2606662988@qq.com"])
        send_mass_mail((("Django邮件1", "Django可以发送邮件", settings.DEFAULT_FROM_EMAIL,
        ["2606662988@qq.com", "2606662988@qq.com"]),
        ("Django邮件2", "Django可以发送邮件", settings.DEFAULT_FROM_EMAIL,
        ["2606662988@qq.com", "2606662988@qq.com"])))
        print('发送成功')
        # return HttpResponse('发送成功')
    except Exception as e:
        print(e)
        return HttpResponseRedirect("发送失败")
    return HttpResponse("发送成功")

# def readerregister(request):
#     if request.method == "GET":
#         return render(request,)

def readerlogin(request):
    """登录"""
    return render(request, 'reader_login.html')
    # return HttpResponse('登录页面')

def register(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'register.html')
        # return HttpResponse('注册页面')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if password != request.POST['password2']:
            error = '密码输入不一致'
            return render(request, 'register.html', {'error': error})
        college = request.POST['college']
        number = request.POST['number']
        email = request.POST['email']
        userinfo = UserInfo(name=username, password=password, school=college, sno=number, email=email)
        userinfo.save()

        return render(request, 'reader_login.html')
        # return HttpResponse('用户注册信息提交数据库成功！')

def ajax(request):
    """ajax"""
    return render(request, 'ajax.html')

def ajaxajax(request):
    """ajaxajax"""
    if request.method == 'GET':
        return HttpResponse('ajaxajax GET请求成功')

    elif request.method == 'POST':
        return HttpResponse('ajaxajax POST请求成功')






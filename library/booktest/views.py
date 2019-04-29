from django.shortcuts import render,redirect,reverse,HttpResponseRedirect,HttpResponse
from .models import UserInfo,BookInfo,BorrowInfo,HotPic,MessageInfo

from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
# Create your views here.

def index(request):
    hotpics = HotPic.objects.all().order_by('index')
    messageinfos = MessageInfo.objects.all()
    return render(request, 'index.html', {'hotpics': hotpics,'messageinfos':messageinfos})

def edit(request):
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

def readerregister(request):
    if request.method == "GET":
        return render(request,)



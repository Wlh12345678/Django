from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    # return HttpResponse('首页')
    postlist = Post.objects.all()

    return render(request,'blogtest/index.html',{'postlist':postlist,'title':'django新闻'})

def detail(request, id):
    postnum = Post.objects.get(pk=id)
    return render(request,'blogtest/single.html', {'postnum':postnum})

from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Post,Category,Tag
from comment.forms import CommentForm
from comment.models import Comment
# Create your views here.

def index(request):
    # return HttpResponse('首页')
    postlist = Post.objects.all()

    return render(request,'blogtest/index.html',{'postlist':postlist,'title':'django新闻'})

def detail(request, id):
    # 详情
    postnum = Post.objects.get(pk=id)
    form = CommentForm()

    # commentnum = Comment.objects.all()

    return render(request,'blogtest/single.html', {'postnum': postnum, 'form': form})

def fullwidth(request):
    # 博客
    return render(request,'blogtest/full-width.html')


def about(request):
    # 关于
    return render(request, 'blogtest/about.html')

def contact(request):
    # 联系
    return render(request, 'blogtest/contact.html')

def archives(request,year,month):
    # 归档
    postlist = Post.objects.all().filter(modified_time__year=year, modified_time__month=month)
    return render(request, 'blogtest/index.html', {'postlist': postlist})

def category(request,id):
    # 分类
    postlist = Category.objects.get(pk=id).post_set.all()
    return render(request, 'blogtest/index.html', {'postlist': postlist})

def tag(request,id):
    # 标签云
    postlist = Tag.objects.get(pk=id).post_set.all()
    return render(request, 'blogtest/index.html', {'postlist': postlist})


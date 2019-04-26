from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Post
from comment.forms import CommentForm
from comment.models import Comment
# Create your views here.

def index(request):
    # return HttpResponse('首页')
    postlist = Post.objects.all()

    return render(request,'blogtest/index.html',{'postlist':postlist,'title':'django新闻'})

def detail(request, id):
    postnum = Post.objects.get(pk=id)
    form = CommentForm()

    # commentnum = Comment.objects.all()

    return render(request,'blogtest/single.html', {'postnum': postnum, 'form': form})



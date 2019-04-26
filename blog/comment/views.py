from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CommentForm
from blogtest.models import Post

# Create your views here.



def comitcoment(request,id):
    """评论功能"""
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('blogtest:detail',args=(id,)))
    else:
        return HttpResponse('评论失败')
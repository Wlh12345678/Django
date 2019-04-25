"""
自动生成表单

"""
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    model = Comment
    fields = ['name', 'email', 'url', 'text']


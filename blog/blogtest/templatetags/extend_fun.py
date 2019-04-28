from django import template
from ..models import Post,Category,Tag
from comment.models import Comment

# 得到Django的负责管理标签和过滤器的类
register = template.Library()

@register.filter(name='mylower')
def mylower(value):
    """
    添加转小写方法
    :param value: 应用过滤器的对象
    :return:
    """
    return value.lower()

"""添加过滤器"""
@register.filter(name='myjoin')
def myjoin(value,sep):
    return value.join(sep)





"""添加标签 按时间顺序展示内容"""
@register.simple_tag
def getlatestposet():
    latepost = Post.objects.all().order_by('-creat_time')[:5]
    return latepost

"""添加标签 展示与文章相同id的评论"""
@register.simple_tag
def get_comment_list(id):
    result = Post.objects.get(pk=id).comment_set.all()
    return result

"""添加标签 展示文章归档日期"""
@register.simple_tag
def getarchives():
    # order = 'DESC' 降序
    archives = Post.objects.all().dates('modified_time', 'month', order='DESC')[:3]
    return archives

"""添加标签 展示文章分类"""
@register.simple_tag
def getcategory():
    category = Category.objects.all()
    return category

"""添加标签，展示标签云"""
@register.simple_tag
def gettag():
    tag = Tag.objects.all()
    return tag













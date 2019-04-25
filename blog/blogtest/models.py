from django.db import models

# Create your models here.

# 分类表
class Category(models.Model):
    cname = models.CharField(max_length=20)
    def __str__(self):
        return self.cname
# 标签表
class Tag(models.Model):
    tname = models.CharField(max_length=20)
    def __str__(self):
        return self.tname
# 文章表
class Post(models.Model):
    ptitle = models.CharField(max_length=50)
    psummary = models.CharField(max_length=200)
    pbody = models.TextField(max_length=100000)
    creat_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    author = models.CharField(max_length=20)
    read = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.ptitle





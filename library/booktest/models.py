from django.db import models

"""建立数据库信息"""

# Create your models here.
"""用户信息"""
class UserInfo(models.Model):
    name = models.CharField(max_length=20)      #用户名
    password = models.CharField(max_length=20)  #密码
    school = models.CharField(max_length=20, null=True, blank=True)    #学院
    sno = models.CharField(max_length=20, null=True, blank=True)       #学号
    email = models.EmailField(max_length=20, null=True, blank=True)    #邮箱


"""图书信息"""
class BookInfo(models.Model):
    isbn = models.IntegerField()                    #ISBN
    name = models.CharField(max_length=20)          #书名
    author = models.CharField(max_length=20)        #作者
    publisher = models.CharField(max_length=20)     #出版商
    publishtime = models.DateTimeField( auto_now_add=True)            #出版时间


"""借阅信息"""
class BorrowInfo(models.Model):
    name = models.CharField(max_length=20)              #借阅者
    borrowtime = models.DateTimeField(auto_now=True)    #借阅日期
    returntime = models.DateTimeField(auto_now=True)    #归还日期
    username = models.ForeignKey('UserInfo', on_delete=models.CASCADE)       #用户外键
    bookname = models.ForeignKey('BookInfo', on_delete=models.CASCADE)       #图书外键

"""图片信息"""
class HotPic(models.Model):
    name = models.CharField(max_length=20)          #名字
    pic = models.ImageField(upload_to='hotpic')     #图片 存储的为图片的相对路径  upload_to 存储位置
    index = models.SmallIntegerField(unique=True)   #排序  unique=True 序号唯一，图片唯一


from tinymce.models import HTMLField

"""富文本"""
class MessageInfo(models.Model):
    title = models.CharField(max_length=20)     #添加富文本
    #富文本字段
    message = HTMLField()
    def __str__(self):
        return self.title



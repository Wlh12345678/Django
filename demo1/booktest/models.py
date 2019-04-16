from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField(auto_now_add=True)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名 第二个参数代表删除时的类型（CASCADEA 级联删除）
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)



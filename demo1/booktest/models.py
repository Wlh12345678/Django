from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=50)
    # 外键 第一个参数为表名 第二个参数代表删除时的类型（CASCADEA 级联删除）
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    def __str__(self):
        return self.hname

    def skill(self):
        return self.hcontent
    skill.short_description = '绝招'

    def sex(self):
        return self.hgender
    sex.short_description = '性别'


"""
python manage.py shell 进入命令：不需要运行项目就可以操作数据库
导入类  from bookset.models import HeroInfo,BookInfo
查找所有行 表名.objects.all()
根据主键查找 表名.objects.get(pk = 1)
添加对象 **.save()
修改    **.save()
删除    **.delete()

一对多：一方存在主键 多方存在主键也存在外键（一方中的主键）

一方.heroinfo_set.all()

类名.objects.create(列名=值)  不需要save
"""

"""
list_display=[]
list_filter=[]
search_fields=[]
list_per_page=10
"""

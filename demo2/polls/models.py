from django.db import models

# Create your models here.

# 创建一个问题数据库
class QuestionInfo(models.Model):
    # 问题
    question = models.CharField(max_length=50)
    # 时间
    qpub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question


# 创建一个投票详情统计数据库
class VoteInfo(models.Model):
    # 选项内容
    option = models.CharField(max_length=50)
    # 投票数
    vnum = models.IntegerField(default=0)
    # 外键 第一个参数为表名 第二个参数代表删除时的类型（CASCADEA 级联删除）
    vquestion = models.ForeignKey('QuestionInfo', on_delete=models.CASCADE)
    def __str__(self):
        return self.option





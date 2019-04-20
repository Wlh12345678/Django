from django.contrib import admin
from .models import BookInfo, HeroInfo, Account, Contact, Host, Application
# Register your models here.

class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    # 关联个数
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle']
    # 将书和主角绑定添加
    inlines = [HeroInfoInlines]

# 注册模型类
admin.site.register(BookInfo,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    # 显示对象指定列  列名  可以点击列头进行排序
    list_display = ['hname', 'sex', 'skill']
    # list_filter 过滤器
    list_filter = ['hname']
    # search_fields 搜索框 支持模糊查询
    search_fields = ['hname','hcontent']
    # list_per_page 分页（3：一页显示3条信息）
    list_per_page = 3


# 注册模型类
admin.site.register(HeroInfo,HeroInfoAdmin)

admin.site.register(Account)
admin.site.register(Contact)
admin.site.register(Host)
admin.site.register(Application)
"""
通过少量代码实现强大的后台管理
需要将特定的数据模型注册 才能在后台管理
"""


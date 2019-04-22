from django.contrib import admin
from .models import QuestionInfo, VoteInfo
# Register your models here.

class VoteInfolines(admin.StackedInline):
    model = VoteInfo
    # 选项每次添加2个
    extra = 2

class QuestionInfoAdmin(admin.ModelAdmin):
    list_display = ['question']
    inlines = [VoteInfolines]

admin.site.register(QuestionInfo,QuestionInfoAdmin)

class VoteInfoAdmin(admin.ModelAdmin):
    list_display = ['option', 'vnum', 'vquestion_id']
    list_filter = ['option']
    search_fields = ['option']
    list_per_page = 5

admin.site.register(VoteInfo,VoteInfoAdmin)



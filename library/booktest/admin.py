from django.contrib import admin
from .models import UserInfo, BookInfo, BorrowInfo,HotPic,MessageInfo

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(BookInfo)
admin.site.register(BorrowInfo)
admin.site.register(HotPic)
admin.site.register(MessageInfo)




from django.conf.urls import url
from . import views

app_name = 'comment'

urlpatterns = [
    # 接收评论信息
    url(r'^comitcoment/(\d+)/$', views.comitcoment, name='comitcoment'),


]




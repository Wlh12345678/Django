from django.conf.urls import url
from . import views
from .feed import PostFeed
app_name = 'blogtest'

urlpatterns = [
    # 首页
    url(r'blogtest/$', views.index, name='index'),
    # 详情页
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    # 博客
    url(r'fullwidth/$', views.fullwidth, name='fullwidth'),
    # 关于
    url(r'about/$', views.about, name='about'),
    # 联系
    url(r'contact/$', views.contact, name='contact'),
    # 搜索单独建立了文件夹
    # 归档
    url(r'archives/(\d+)/(\d+)/$', views.archives, name='archives'),
    # 分类
    url(r'category/(\d+)/$', views.category, name='category'),
    # 标签云
    url(r'tag/(\d+)/$', views.tag, name='tag'),
    # RSS
    url(r'^rss/$', PostFeed(), name='rss')

]




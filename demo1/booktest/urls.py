from django.conf.urls import url
from .import views

# 去除硬编码'booktest'与demo1中的urls.py中的 url内的namespace对应
app_name = 'booktest'

urlpatterns = [
    # url('index/',views.index),
    # url('index/$',views.index),
    url(r'^$', views.index,name='index'),
    url(r'^list/$', views.list,name='list'),
    # (\d+) 详情页页码
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
]



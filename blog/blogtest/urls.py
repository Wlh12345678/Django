from django.conf.urls import url
from . import views
from .feed import PostFeed
app_name = 'blogtest'

urlpatterns = [
    url(r'blogtest/$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),

    url(r'^rss/$',PostFeed(),name='rss')


]




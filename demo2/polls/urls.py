from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^index/$', views.Index, name='index'),
    url(r'^detail/(\d+)/$', views.Detail, name='detail'),
    url(r'^votehandler/$', views.VoteHandler, name='votehandler'),
    url(r'^result/(\d+)/$', views.Result, name='result'),
]






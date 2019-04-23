from django.conf.urls import url
from . import views

app_name = 'extendtest'

urlpatterns = [
    url(r'^list/$', views.list, name='list'),

]



from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'index/$', views.index, name='index'),
    url(r'edit/$', views.edit, name='edit'),
    url(r'sendemail/$', views.sendemail, name='sendemail'),
]




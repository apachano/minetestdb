from django.conf.urls import url

from . import views

app_name = 'servers'
urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^/(?P<name>\w+)/$', views.detail, name='detail'),
    url(r'^-new/$', views.new, name='new'),
]

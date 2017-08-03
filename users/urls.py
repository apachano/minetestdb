from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
]

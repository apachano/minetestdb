from django.conf.urls import url

from . import views

app_name = 'mods'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>\w+)/$', views.detail, name='detail'),
]
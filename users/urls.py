from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^/(?P<username>\w+)/$', views.detail, name='detail'),
    url(r'^/(?P<username>\w+)/profile/$', views.profile, name='profile'),
    url(r'^-logout/', views.logout_view, name='logout'),
    url(r'^-login/', views.login_view, name='login'),
]

from django.conf.urls import url

from . import views

app_name = 'servers'
urlpatterns = [
    url(r'^/$', views.index, name='index'),

    # NOTE:
    # r'^/(?P<name>\w+)/detail' matches all alphanumeric, no whitespace chars
    # the current implementation matches all characters
    #
    # IF YOU EVER HAVE THIS PROBLEM AGAIN RESEARCH YOUR REGEX:
    #	https://docs.python.org/3/howto/regex.html
    #	https://docs.python.org/3/library/re.html
    #
    url(r'^/(?P<name>.(?s)+)/detail', views.detail, name='detail'),
    url(r'^-new/$', views.new, name='new'),
    url(r'^/(?P<name>.(?s)+)/edit', views.edit, name='edit'),
]

from django.shortcuts import get_object_or_404, render

from .models import Server
from .models import Tag


def index(request):
    current_server_list = Server.objects.all()
    tags = Tag.objects.all()
    mt_version = ["0.4.16", "0.5.0"]
    subgame = 0
    filters = {'Tags': tags, 'Mt_Version': mt_version}

    context = {'current_server_list': current_server_list,
               'filters': filters}
    return render(request, 'servers/index.html', context)


def detail(request, name):
    server = get_object_or_404(Server, name=name)
    return render(request, 'servers/detail.html', {'server': server})

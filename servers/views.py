from django.shortcuts import get_object_or_404, render

from .models import Server
from .models import Tag


def index(request):
    current_server_list = Server.objects.all()
    if request.method == 'POST':
        post = request.POST
        for tag in post:
            if tag != 'csrfmiddlewaretoken':
                current_server_list = current_server_list.filter(tags=tag)
    else:
        post = {}

    tags = Tag.objects.all()
    mt_version = ["0.4.16", "0.5.0"]
    filters = {'Tags': tags, 'Minetest Version': mt_version}

    context = {'current_server_list': current_server_list,
               'filters': filters,
               'post': post}
    return render(request, 'servers/index.html', context)


def detail(request, name):
    server = get_object_or_404(Server, name=name)
    return render(request, 'servers/detail.html', {'server': server})

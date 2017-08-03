from django.shortcuts import get_object_or_404, render

from .models import Server


def index(request):
    current_server_list = Server.objects.all()
    filter_tags = ["pvp", "protection", "economy"]
    filter_mt_version = ["0.4.16", "0.5.0"]
    filter_subgame = 0

    context = {'current_server_list': current_server_list ,
               'filters_tags': filter_tags ,
               'filters_mt_version': filter_mt_version ,
               'filters_subgame': filter_subgame}
    return render(request, 'servers/index.html', context)


def detail(request, server_name):
    server = get_object_or_404(Server, server_name=server_name)
    return render(request, 'servers/detail.html', {'server': server})

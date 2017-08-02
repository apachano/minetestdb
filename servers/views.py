from django.shortcuts import get_object_or_404, render

from .models import Server


def index(request):
    current_server_list = Server.objects.order_by('-server_votes')[:10]
    context = {'current_server_list': current_server_list}
    return render(request, 'servers/index.html', context)


def detail(request, server_name):
    server = get_object_or_404(Server, server_name=server_name)
    return render(request, 'servers/detail.html', {'server': server})

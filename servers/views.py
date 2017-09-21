from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Server
from .models import Tag
from .forms import NewServerForm


def index(request):
    current_server_list = Server.objects.all()
    if request.method == 'POST':
        post = request.POST
        # if post.sort == 'Oldest':
        #     current_server_list = Server.objects.order_by('id')
        # if post.sort == 'Newest':
        #     current_server_list = Server.objects.order_by('-id')
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


def new(request):
    if request.method == 'POST':
        form = NewServerForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            model.save()
            return render(request, 'servers/confirm.html', {'form': form})
    else:
        form = NewServerForm()

    return render(request, 'servers/create.html', {'form': form})


def edit(request, name):
    server = get_object_or_404(Server, name=name)
    form = NewServerForm(initial={'name': server.name, 'address': server.address, 'website': server.website,
                                  'description': server.description, 'mt_version': server.mt_version,
                                  })
    return render(request, 'servers/edit.html', {'server': server, 'form': form})

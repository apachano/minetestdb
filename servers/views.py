from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#END CONSTRUCTORS AND LIBS

# NOTE: Global Imports
from universal import (
    #Version (Redundant)
    dynamic_sort
)

# NOTE: Local Imports
from .models import (
    Server,
    Tag,
    Version
)
from .forms import (
    NewServerForm
)


def index(request):
    tags = Tag.objects.all()
    versions = Version.objects.all()
    servers = Server.objects.all()

    # Here, we sort the post data.
    # It's alot more efficient to do it here than from within the templates
    #
    if request.method == 'POST':
        post = request.POST.dict()
        sorted_servers = dynamic_sort(post, servers, [Tag, Version])
    else:
        post = {}

    filters = {
        'Minetest Version': versions,			# Available Version Filters
        'Tags': tags 							# Available Filter Tags
    }

    # This is just a rebinding of variables in python scope, to template scope.
    context = {
        'post': post,							# Raw Post
        'servers': sorted_servers,				# Available Servers
        'filters': filters						# All Available Filters
    }
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
            form.save_m2m()
            return render(request, 'servers/confirm.html', {'form': form})
    else:
        form = NewServerForm()

    return render(request, 'servers/create.html', {'form': form})


def edit(request, name):
    server = get_object_or_404(Server, name=name)
    if request.method == 'POST':
        form = NewServerForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            model.save()
            form.save_m2m()
            return render(request, 'servers/confirm.html', {'form': form})
    else:
        form = NewServerForm({'name': server.name,
                              'address': server.address,
                              'website': server.website,
                              'description': server.description,
                              'mt_version': server.mt_version,
                              'tags': server.tags
                              })

    return render(request, 'servers/edit.html', {'server': server, 'form': form})

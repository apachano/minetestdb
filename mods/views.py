from django.shortcuts import get_object_or_404, render
#END CONSTRUCTORS AND LIBS

# NOTE: Global Imports
from universal import (
	# Version # don't need this here because it's inherited through our local .models
)

# NOTE: Local Imports
from .models import (
	Mod,
	Tag,
	Version
)
from .forms import (
	NewModForm
)


def index(request):
    current_mod_list = Mod.objects.all()
    if request.method == 'POST':
        post = request.POST
        for tag in post:
            if tag != 'csrfmiddlewaretoken':
                current_mod_list = current_mod_list.filter(tags=tag)
    else:
        post = {}

    tags = Tag.objects.all()
    versions = Version.objects.all()
    filters = {'Minetest Version': versions, 'Tags': tags}

    context = {'current_mod_list': current_mod_list,
               'filters': filters,
               'post': post}
    return render(request, 'mods/index.html', context)


def detail(request, name):
    mod = get_object_or_404(Mod, name=name)
    return render(request, 'mods/detail.html', {'mod': mod})


def new(request):
    if request.method == 'POST':
        form = NewModForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.author = request.user
            page = model.name
            model.save()
            return render(request, 'mods/' + page, {'form': form})
    else:
        form = NewModForm()

    return render(request, 'mods/create.html', {'form': form})


def edit(request, name):
    server = get_object_or_404(Server, name=name)
    form = NewServerForm(initial={'name': server.name,
                                  'address': server.address,
                                  'website': server.website,
                                  'description': server.description,
                                  'mt_version': server.mt_version,
                                  'tags': server.tags
                                  })
    return render(request, 'servers/edit.html', {'server': server, 'form': form})

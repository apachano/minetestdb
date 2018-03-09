from django.shortcuts import get_object_or_404, render
#END CONSTRUCTORS AND LIBS

# NOTE: Global Imports
from universal import (
    # Version # don't need this here because it's inherited through our local .models
    dynamic_sort
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
    mods = Mod.objects.all()
    tags = Tag.objects.all()
    versions = Version.objects.all()

    # Here, we sort the post data.
    # It's alot more efficient to do it here than from within the templates
    #
    if request.method == 'POST':
        post = request.POST.dict()
        mods = dynamic_sort(post, mods, [Tag, Version])
    else:
        post = {}


    filters = {
        'Minetest Version': versions,			# Available Version Filters
        'Tags': tags 							# Available Filter Tags
    }

    # This is just a rebinding of variables in python scope, to template scope.
    context = {
        'post': post,							# Raw Post
        'mods': mods,							# Available Mods
        'filters': filters						# All Available Filters
    }
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

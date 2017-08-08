from django.shortcuts import get_object_or_404, render

from .models import Mod
from .models import Tag


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
    mt_version = ["0.4.16", "0.5.0"]
    filters = {'Tags': tags, 'Minetest Version': mt_version}

    context = {'current_mod_list': current_mod_list,
               'filters': filters,
               'post': post}
    return render(request, 'mods/index.html', context)


def detail(request, name):
    mod = get_object_or_404(Mod, name=name)
    return render(request, 'mods/detail.html', {'mod': mod})

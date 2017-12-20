from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Server
from .models import Tag
from .forms import NewServerForm


def index(request):
    servers = Server.objects.all()
    if request.method == 'POST':
        post = request.POST.dict()
	"""
        # if post.sort == 'Oldest':
        #     current_server_list = Server.objects.order_by('id')
        # if post.sort == 'Newest':
        #     current_server_list = Server.objects.order_by('-id')
        for tag in post:
            if tag != 'csrfmiddlewaretoken':
                servers = servers.filter(tags=tag)
        """
    else:
        post = {}

    # NOTE:
    #	The models are essentially a python equivalent of sql tables
    #	but there's the added ability for you to work with them directly in the
    #	language
    #
    #	So when you're testing things. Instead of making a new structure to debug
    #	your code, you just add to the sql database. Which you can do by calling
    #	python manage.py shell; # Which will open a python shell. Then...
    #		from servers.models import Server # imports our database model
    #		a = Server(name="immagoodname", version="1.2.3", ...) #create a new entry
    #		a.save() #save the entry in our sql database
    #
    #	# exit and restart manage.py shell:
    #		from servers.models import Servers
    #		servers = Server.objects.all() # this should now be populated with query objects
    #		# will return : <QuerySet [<Server: Server object (1)...>]>
    #
    #	# If you're having trouble with the data for any reason or need to delete it:
    #	python manage.py flush
    #		or "depending on your django version"
    #	python manage.py reset <APPNAME>
    #
    #
    # servers = Server.objects.all() #[[[ Just so I remember it's here... ]]]#
    #
    print(post)
    print(post.keys())

    #	This is just a rebinding of variables in python scope, to template scope.
    context = {
        'post': post,							# Raw Post
        'servers': servers						# Top level
        #'version': servers[n].version			# we'll access this from template scope
												# with the "servers" data structure above
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
            return render(request, 'servers/confirm.html', {'form': form})
    else:
        form = NewServerForm()

    return render(request, 'servers/create.html', {'form': form})


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

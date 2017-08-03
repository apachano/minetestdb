from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from django.contrib.auth.models import User


def index(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'users/index.html', context)


def detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/detail.html', {'user': user})

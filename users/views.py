from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Lists registered users
def index(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'users/index.html', context)


# Displays information on a user
def detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/detail.html', {'duser': user})


# Allows user to edit their profile
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        return render(request, 'users/profile.html')


def logout_view(self, request):
    logout(request)
    redirect("/")
    return


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect("/")
    else:
        redirect("/")


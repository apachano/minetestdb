from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from servers.models import Server
from mods.models import Mod
from users.forms import ChangeContactForm


# Lists registered users
def index(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'users/index.html', context)


# Displays information on a user
def detail(request, username):
    user = get_object_or_404(User, username=username)
    server_list = Server.objects.filter(owner=user)
    mod_list = Mod.objects.filter(author=user)
    return render(request, 'users/detail.html', {'duser': user,
                                                 'servers': server_list,
                                                 'mods': mod_list})


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


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


def change_contact(request):
    if request.method == 'POST':
        form = ChangeContactForm(request.POST)
        if form.is_valid():
            prof = request.user.profile
            if form.cleaned_data['github']:
                prof.github = form.cleaned_data['github']
            prof.save()
            return redirect('users:change_contact')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangeContactForm()
    return render(request, 'users/change_contact.html', {
        'form': form.as_p()
    })

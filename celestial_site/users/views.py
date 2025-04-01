from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:celestial_list')) 
        
 
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', context={'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login')) 


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, Successful Registration')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile was changed')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})
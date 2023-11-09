from typing import Set
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout, authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .forms import CusRatFeedform

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account is created Successfully.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form':form})


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    # if else block to check user is superuser or authenticated or invalid user

    if user is None:
        messages.success(
        request,
        'Invalid login try again'
        )
        return redirect('login')

    elif user.is_superuser:
        messages.success(
        request,
        f'{username},is a superuser and have been logged In successfully'
        )
        login(request,user)
        return redirect('food:index')

    elif user is not None:
        messages.success(
        request,
        f'{username},you have been logged In successfully'
        )
        login(request,user)
        return redirect('food:index')


def logout_view(request):
    username = request.user.username
    messages.success(request, f'{username}, you have been logged out successfully')
    logout(request)
    return redirect('food:index')



@login_required
def profilepage(request):
    return render(request, 'users/profile.html')


def CusRatFeed(request, pc):
    form = CusRatFeedform(request.POST or None)

    if form.is_valid():
        form.instance.prod_code = pc
        form.save()
        return redirect('food:index')

    return render(request, 'users/item-form.html', {'form':form})
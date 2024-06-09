from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditProfileForm
from food.models import Item
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def profilepage(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'profile.html', {'items': items})

def logout_user(request):
    logout(request)
    return redirect('login')

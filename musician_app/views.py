from album_app.models import Album_Model
from .forms import MusicianModel_Form, MusicianModelUpdate_Form

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def musician_signup(request):
    if request.method == 'POST':
        form = MusicianModel_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            messages.success(request, f'Welcome {user}! Your account has been created successfully!')
            return redirect('login')
    else:
        form = MusicianModel_Form()
    context = {'form': form, 'type': 'Sign Up'}
    return render(request, './musician_app/signup_musician.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def musician_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}! Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('signup')
    else:
        form = AuthenticationForm()
    context = {'form': form, 'type': 'Login'}
    return render(request, './musician_app/login_musician.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def musician_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def show_musician_profile(request):
    profile = User.objects.get(username=request.user.username)
    my_albums = Album_Model.objects.filter(musician=profile)
    context = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'email': profile.email,
        'my_albums': my_albums,
    }
    return render(request, './musician_app/profile_musician.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def edit_musician_profile(request):
    if request.method == 'POST':
        form = MusicianModelUpdate_Form(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Your profile information has been updated successfully.')
            return redirect('profile')
    else:
        form = MusicianModelUpdate_Form(instance=request.user)
    context = {'form': form, 'type': 'Edit'}
    return render(request, './musician_app/edit_musician.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def delete_musician_profile(request):
    musician = request.user
    messages.success(request, f'{musician.username}\'s profile information has been deleted successfully!')
    musician.delete()
    return redirect('signup')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def change_musician_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form, 'type': 'Change'}
    return render(request, './musician_app/change_password.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def reset_user_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('login')
    else:
        form = SetPasswordForm(request.user)
    context = {'form': form, 'type': 'Reset'}
    return render(request, './musician_app/reset_password.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

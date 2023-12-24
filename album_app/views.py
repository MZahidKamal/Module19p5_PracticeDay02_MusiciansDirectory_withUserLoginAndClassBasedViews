from django.shortcuts import render, redirect
from .forms import AlbumModel_Form
from .models import Album_Model
from django.contrib.auth.decorators import login_required

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def add_album(request):
    if request.method == 'POST':
        form = AlbumModel_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile')
    else:
        form = AlbumModel_Form()
    context = {'form': form}
    return render(request, './album_app/add_album.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def edit_album(request, album_id):
    album_from_db = Album_Model.objects.get(pk=album_id)
    form = AlbumModel_Form(instance=album_from_db)
    if request.method == 'POST':
        form = AlbumModel_Form(request.POST, instance=album_from_db)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile')
    context = {'form': form}
    return render(request, './album_app/edit_album.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def delete_album(request, album_id):
    album_from_db = Album_Model.objects.get(pk=album_id)
    album_from_db.delete()
    return redirect('profile')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

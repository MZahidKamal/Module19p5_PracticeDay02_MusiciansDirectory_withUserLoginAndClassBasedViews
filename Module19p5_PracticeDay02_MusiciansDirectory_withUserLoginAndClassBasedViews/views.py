from django.shortcuts import render
from album_app.models import Album_Model

def base(request):
    return render(request, 'base.html')

def home(request):
    albums = Album_Model.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'index.html', context)

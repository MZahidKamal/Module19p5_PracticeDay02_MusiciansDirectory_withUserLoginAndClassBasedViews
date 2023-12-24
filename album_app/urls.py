from django.urls import path
from .views import add_album, edit_album, delete_album

urlpatterns = [
    path('albums/add_album/', add_album, name='add_album'),
    path('albums/edit_album/<int:album_id>/', edit_album, name='edit_album'),
    path('albums/delete_album/<int:album_id>/', delete_album, name='delete_album'),
]

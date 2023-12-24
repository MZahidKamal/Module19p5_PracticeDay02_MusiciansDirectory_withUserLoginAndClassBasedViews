from django.urls import path
from .views import musician_signup, musician_login, musician_logout, show_musician_profile, edit_musician_profile, delete_musician_profile, change_musician_password, reset_user_password

urlpatterns = [
    path('musicians/signup/', musician_signup, name='signup'),
    path('musicians/login/', musician_login, name='login'),
    path('musicians/logout/', musician_logout, name='logout'),

    path('musicians/profile/', show_musician_profile, name='profile'),
    path('musicians/edit_profile/', edit_musician_profile, name='edit_profile'),
    path('musicians/delete_profile/', delete_musician_profile, name='delete_profile'),

    path('musicians/change_password/', change_musician_password, name='change_password'),
    path('musicians/reset_password/', reset_user_password, name='reset_password'),
]

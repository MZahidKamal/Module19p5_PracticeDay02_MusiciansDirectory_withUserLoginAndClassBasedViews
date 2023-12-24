from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

# class MusicianModel_Form(forms.ModelForm):
#     class Meta:
#         model = Musician_Model
#         fields = '__all__'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# instruments_model = Instrument_Model.objects.all()

class MusicianModel_Form(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
        ]

class MusicianModelUpdate_Form(UserChangeForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'id': 'required'}))
    password = None

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]

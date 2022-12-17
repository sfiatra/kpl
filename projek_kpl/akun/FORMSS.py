from django import forms
from .models import UserProfileInfo, Kategori, Film, Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ('nama', 'user')

class LoginForm(forms.Form):
    username = forms.CharField()
    password forms.CharField(widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('nama', 'user')

class UserEditProfile(forms.ModelForm):
    class Meta():
        model = User
        fields = ('nama', 'user')

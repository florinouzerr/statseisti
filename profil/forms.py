
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditProfilForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password')


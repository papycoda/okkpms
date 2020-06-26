from django import forms
from .models import *
class user_loginforms(forms.ModelForm):
    class Meta:
        model = user_login
        widgets = {'password': forms.PasswordInput()}
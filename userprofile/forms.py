from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')
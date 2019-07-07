from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image','bio']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        fields = ['name','location','population','image']


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','description','email']
class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post']

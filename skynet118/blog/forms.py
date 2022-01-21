from django import forms
from django.core.exceptions import ValidationError
from .models import (
        UserProfile,
        Portfolio,
        Comment
        )

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio 
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = '__all__'

# Models for the user registration

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        #fields = '__all__' # not recommended 
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2'] 


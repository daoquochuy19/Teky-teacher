from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField( widget=forms.EmailInput(attrs= {'class' : 'form-control c-placeholder-login'}))

    class Meta:
        model = get_user_model()
        fields = ('username','email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']       
        if commit:
            user.save()
            
        return user
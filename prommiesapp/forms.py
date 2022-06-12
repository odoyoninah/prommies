from django import forms
from .models import Prommies, Profile
from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class PrommiesForm(forms.ModelForm):
    class Meta:
        model = Prommies
        fields = ['name', 'description', 'score', 'link', 'image', 'email', 'my_file']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name', 'email', 'phone', 'address', 'image']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

from django.forms import Form
from.forms import PrommiesForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from .models import Prommies, Profile
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

def index(request):
    prommies=Prommies.objects.all()
    return render(request,'index.html',{'form':Form})

@login_required(login_url='/accounts/login/')
def createpost(request):
    if request.method=='POST':
        form = PrommiesForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('index')
    else:
        form = PrommiesForm()
    return render(request,'createpost.html',{'form':form}) 


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()


   

        return redirect('login')
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})

    
def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('index')


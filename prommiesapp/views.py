import email
from multiprocessing import context
from django.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from prommiesapp.models import Prommies,Profile
from .forms import PrommiesForm, RegisterForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#handle all the status code responses.
from .serializer import PrommiesSerializer, ProfileSerializer


class PrommiesView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        all_prommies = Prommies.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = PrommiesSerializer(all_prommies, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = PrommiesSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        all_profile = Profile.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = ProfileSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    prommies=Prommies.objects.all()
    return render(request,'index.html',{'form':Form})



def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('login')
    
def apikey(request):
    return render(request,'apikey.html')


def projects(request):
    prommies = Prommies.objects.all()
    return render(request,'projects.html',{'prommies':prommies})



@login_required(login_url='/accounts/login/')
def uploadproject(request):
    if request.method=='POST':
        form = PrommiesForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('projects')
    else:
        form = PrommiesForm()
    return render(request,'uploadproject.html',{'form':form}) 


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()


   

        return redirect('login')
        
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})

def search_name(request):
    if 'search' in request.GET and request.GET['search']:
        search_name = request.GET.get('search')
        my_search_results = Prommies.get_name(search_name)
        return render(request,'search.html',{'results':my_search_results})

    else:
        message = 'You have not searched for anything'
        return render(request,'search.html',{'message':message})

    
def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('index')


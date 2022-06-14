import email
from django.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Prommies, User
from .forms import PrommiesForm, RegisterForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#handle all the status code responses.
from .models import Prommies
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

def index(request):
    prommies=Prommies.objects.all()
    return render(request,'index.html',{'form':Form})
    



@login_required(login_url='/accounts/login/')
def uploadproject(request):
    if request.method=='POST':
        form = PrommiesForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('index')
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

    
def logout(request):
    logout(request)
    messages.success(request,'You have successfully logged out!')
    return redirect('index')


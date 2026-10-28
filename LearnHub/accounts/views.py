from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django import forms


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("this is homepage")

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)

            if user.is_superuser or user.groups.filter(name='Admin').exists():
                return redirect('/Admin/')

            elif user.groups.filter(name='Instructor').exists():
                return redirect('/dashboard/')

            elif user.groups.filter(name='Student').exists():
                return redirect('/dashboard/')

            return redirect('/dashboard/')
        
    return render(request,'accounts/login.html',{
                'error':'invalid username or password'
    })

def logout_view(request):
    logout(request)
    return redirect('login')
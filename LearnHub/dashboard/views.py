from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard_home(request):
    user=request.user

    if user.is_superuser or user.groups.filter(name='Admin').exists():
        message="Welcome Admin!"

    elif user.groups.filter(name='Instructor').exists():
        message="welcome to instructor!"

    elif user.groups.filter(name='Student').exists():
        message="welcome student"
    else:
        message="You don't have an assigned role."

    return render(request,'dashboard/dashboard.html',{
        'message':message
    })

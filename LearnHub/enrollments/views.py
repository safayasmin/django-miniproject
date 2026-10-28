from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def enrollment_list(request):
    return HttpResponse("welcome to enrollment ")
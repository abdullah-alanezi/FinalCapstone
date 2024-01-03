from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def home_view(request:HttpRequest):
    investors= User.objects.filter(groups__name='Investors')


    return render(request,'home/home.html',{"investors":investors})


def page_not_found_view(request:HttpRequest):

    return render(request,'home/page_not_found.html')



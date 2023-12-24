from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home_view(request:HttpRequest):

    return render(request,'home/home.html')


def page_not_found_view(request:HttpRequest):

    return render(request,'home/page_not_found.html')



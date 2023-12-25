from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import StartUp


# Create your views here.


def create_startup_view(request:HttpRequest):
    massgae = None

    if request.method == 'POST':
        try:
            new_stratup = StartUp(
                user= request.user,
                startup_name= request.POST['startup_name'],
                startup_avatar=request.FILES['startup_avatar'],
                startup_sector=request.POST['startup_sector'],
                startup_websits=request.POST['startup_websits'],
                startup_email=request.POST['startup_email'],
                startup_number=request.POST['startup_number'],
                startup_description=request.POST['startup_description'],
                startup_founder_name=request.POST['startup_founder_name'],
                startup_target_market=request.POST['startup_target_market']
                )
            new_stratup.save()
        except Exception as e:
            massgae = f'somwthing went wrong {e}'
    return render(request,'startup/create_startup.html',{'massage':massgae,'sectors':StartUp.sectors})
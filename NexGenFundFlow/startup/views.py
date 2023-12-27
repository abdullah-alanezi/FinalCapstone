from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import StartUp,TeamMember


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
            return redirect('startup:view_all_my_stratup_view',user_id=request.user.id)
        except Exception as e:
            massgae = f'somwthing went wrong {e}'
    return render(request,'startup/create_startup.html',{'massage':massgae,'sectors':StartUp.sectors})


def edit_startup_view(request:HttpRequest,startup_id):
    startup = StartUp.objects.get(id=startup_id)

    if request.method == 'POST':
        startup.startup_description = request.POST['startup_description']
        startup.startup_name= request.POST['startup_name']
        startup.startup_sector=request.POST['startup_sector']
        startup.startup_websits=request.POST['startup_websits']
        startup.startup_email=request.POST['startup_email']
        startup.startup_number=request.POST['startup_number']
        startup.startup_founder_name=request.POST['startup_founder_name']
        startup.startup_target_market=request.POST['startup_target_market']

        if 'startup_avatar' in request.FILES:
            startup.startup_avatar=request.FILES['startup_avatar']
        
        startup.save()

        return redirect('startup:view_all_my_stratup_view',user_id=request.user.id)




    return render(request,'startup/edit_startup.html',{'startup':startup,'sectors':StartUp.sectors})

def view_all_my_stratup_view(request:HttpRequest,user_id):

    startup = StartUp.objects.filter(user=user_id)

    return render(request,'startup/all_my_startup.html',{'startup':startup})

def view_startup_profile_view(request:HttpRequest,startup_id):
    startup = StartUp.objects.get(id=startup_id)

    return render(request,'startup/view_startup.html',{'startup':startup})

def team_view(request:HttpRequest,startup_id):

    massage = None
    team = TeamMember.objects.all().count()
    if team == 0:
        massage = "You don't have a team yet"
    
    member = TeamMember.objects.filter(startup=startup_id)


    return render(request,'startup/view_team_member.html',{'massage':massage,'member':member})


def add_team_member_view(request:HttpRequest,startup_id):
    startup = StartUp.objects.get(id=startup_id)
    massage = None
    if request.method == 'POST':
        member = TeamMember(
            startup=startup,
            team_name= request.POST['team_name'],
            team_avatar=request.FILES['team_avatar'],
            team_role=request.POST['team_role'],
            team_linkdin=request.POST['team_linkdin']
            )
        member.save()
        return redirect('startup:view_startup_profile_view',startup_id=startup_id)
    
    return render(request,'startup/add_team_member.html',{'massage':massage,'startup_id':startup_id})
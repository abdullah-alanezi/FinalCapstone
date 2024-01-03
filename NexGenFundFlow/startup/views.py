from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import StartUp,TeamMember,FundingRound
from fund.models import InvestmentOffer
from django.shortcuts import get_object_or_404


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
    team = TeamMember.objects.filter(startup=startup)
    return render(request,'startup/view_startup.html',{'startup':startup,'team':team})

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



def all_funding_round_view(request:HttpRequest,startup_id):
    new = StartUp.objects.get(id=startup_id)

    search = FundingRound.objects.filter(startup=new)

    return render(request,'startup/view_funding_round.html',{'fund':search})



def disapprove_request_view(request, request_id):
    investment_request = get_object_or_404(InvestmentOffer, id=request_id)
    investment_request.status = 'Disapproved'
    investment_request.save()
    return redirect('startup:view_funding_request', startup_id=investment_request.funding_round.startup.id)


def funding_round_view(request:HttpRequest,startup_id):
    sit = StartUp.objects.get(id=startup_id)

    if request.method == 'POST':
        fund = FundingRound(
            startup=sit,
            fund_percentage= request.POST['fund_percentage'],
            fund_amount= request.POST['fund_amount'],
            fund_stage= request.POST['fund_stage'],
        )
        fund.save()
        return redirect('startup:all_funding_round_view',startup_id=startup_id)
    
    return render(request,'startup/funding_round.html',{'stage':FundingRound.stages,'startup_id':startup_id})

def approved_reqeust_view(request:HttpRequest, request_id):
    if request.method == 'POST':
        investment_request = InvestmentOffer.objects.get(id=request_id)
        investment_request.status = 'Approved'
        investment_request.save()
       
        return redirect('startup:view_funding_request', startup_id=investment_request.funding_round.startup.id)

def view_funding_request(request: HttpRequest, startup_id):
    new = StartUp.objects.get(id=startup_id)
    funding_rounds = FundingRound.objects.filter(startup=new)
    investment_requests = InvestmentOffer.objects.filter(funding_round__in=funding_rounds)
    return render(request, 'startup/accept_request.html', {"investment_requests": investment_requests})

def disapproved_reqeust_view(request, request_id):
    investment_request = get_object_or_404(InvestmentOffer, id=request_id)
    investment_request.status = 'Disapproved'
    investment_request.save()
    return redirect('startup:view_funding_request', startup_id=investment_request.funding_round.startup.id)

def view_all_funding_request(request:HttpRequest,user_id):
    investment_requests = InvestmentOffer.objects.filter(user=user_id)

    return render(request,'startup/all_funding_request.html', {"investment_requests": investment_requests})

def funding_request_view(request:HttpRequest,funding_id):

    funding_rounds = FundingRound.objects.filter(startup=funding_id)
    investment_requests = InvestmentOffer.objects.filter(funding_round__in=funding_rounds)
    return render(request, 'startup/accept_request.html', {"investment_requests": investment_requests})

def edit_member_profile_view(request:HttpRequest,member_id):
    team = TeamMember.objects.get(id=member_id)

    return render(request,'startup/edit_member_profile.html',{'team':team})

def delete_member_view(request:HttpRequest,member_id):
    team = TeamMember.objects.get(id=member_id)
    team.delete()
    return redirect('startup:view_startup_profile_view',startup_id=team.startup.id)

def edit_member(request:HttpRequest,member_id):
    team = TeamMember.objects.get(id=member_id)
    
    if request.method == 'POST':
        team.team_name = request.POST['team_name']
        team.team_linkdin = request.POST['team_linkdin']
        team.team_role = request.POST['team_role']
    
        if 'team_avatar' in request.FILES:
            team.team_avatar = request.FILES['team_avatar']
        else:
            team.save()
            return redirect('startup:edit_member_profile_view',member_id=member_id)
        
    return render(request,'startup/edit_member.html',{'team':team})
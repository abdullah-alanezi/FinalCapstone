from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
from startup.models import FundingRound

# Create your views here.

def all_funding_round_view(request:HttpRequest):
    funding_rounds = FundingRound.objects.all()
    funding_rounds_count = funding_rounds.count()
    
    return render(request,"fund/all_funding_round.html",{"funding_rounds":funding_rounds,"funding_rounds_count":funding_rounds_count})

def funding_round_details_view(request:HttpRequest,funding_round_id):
    funding_round = FundingRound.objects.get(id = funding_round_id)
    
    return render(request,"fund/funding_round_details.html",{"funding_round":funding_round})

    
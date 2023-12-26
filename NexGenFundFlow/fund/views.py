from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
from startup.models import FundingRound 
from .models import InvestmentOffer

# Create your views here.

def all_funding_round_view(request:HttpRequest):
    funding_rounds = FundingRound.objects.all()
    funding_rounds_count = funding_rounds.count()
    
    return render(request,"fund/all_funding_round.html",{"funding_rounds":funding_rounds,"funding_rounds_count":funding_rounds_count})

def funding_round_details_view(request:HttpRequest,funding_round_id):
    funding_round = FundingRound.objects.get(id = funding_round_id)
    if request.method == "POST":
        new_investment_offer = InvestmentOffer(user=request.user ,funding_round=funding_round, percentage=request.POST["percentage"], amount=request.POST["amount"])
        new_investment_offer.save()
        
        return redirect("fund:investment_requests_view")
    
    return render(request,"fund/funding_round_details.html",{"funding_round":funding_round})

def investment_requests_view(request:HttpRequest):
    investment_requests = InvestmentOffer.objects.filter(user=request.user)
    count = 0
    
    return render(request,"fund/investment_requests.html",{"investment_requests":investment_requests, "count":count})

def cancel_investment_offer_view(request:HttpRequest,investment_offer_id):
    investment_offer = InvestmentOffer.objects.get(id=investment_offer_id)
    investment_offer.delete()
    return redirect("fund:investment_requests_view")
    



    
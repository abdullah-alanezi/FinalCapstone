from django.shortcuts import render ,redirect
from django.http import HttpRequest , HttpResponse
from startup.models import FundingRound 
from .models import InvestmentOffer , InvestmentOfferComment
from django.contrib.auth.models import User

# Create your views here. 



def all_funding_round_view(request:HttpRequest):
    funding_rounds = FundingRound.objects.all()
    funding_rounds_count = funding_rounds.count()
    investors= User.objects.filter(groups__name='Investors')

    
    
    return render(request,"fund/all_funding_round.html",{"funding_rounds":funding_rounds,"funding_rounds_count":funding_rounds_count,"investors":investors})
def funding_round_details_view(request:HttpRequest,funding_round_id):
    investors= User.objects.filter(groups__name='Investors')
    
    funding_round = FundingRound.objects.get(id = funding_round_id)
    
    if request.method == "POST":
        new_investment_offer = InvestmentOffer(user=request.user ,funding_round=funding_round, percentage=request.POST["percentage"], amount=request.POST["amount"])
        new_investment_offer.save()
        
        return redirect("fund:investment_requests_view")
    
    return render(request,"fund/funding_round_details.html",{"funding_round":funding_round,'investors':investors})

def investment_requests_view(request:HttpRequest):
    
    investors= User.objects.filter(groups__name='Investors')

    investment_requests = InvestmentOffer.objects.filter(user=request.user)
    if "filter" in request.GET and request.GET["filter"]=="Pending":
        investment_requests = InvestmentOffer.objects.filter(user=request.user,status="Pending")
    if "filter" in request.GET and request.GET["filter"]=="Approved":
        investment_requests = InvestmentOffer.objects.filter(user=request.user,status="Approved")
    if "filter" in request.GET and request.GET["filter"]=="Disapproved":
        investment_requests = InvestmentOffer.objects.filter(user=request.user,status="Disapproved")
    if "filter" in request.GET and request.GET["filter"]=="Canceled":
        investment_requests = InvestmentOffer.objects.filter(user=request.user,status="Canceled")
    
        

    
    return render(request,"fund/investment_requests.html",{"investment_requests":investment_requests,"investors":investors})

def cancel_investment_offer_view(request:HttpRequest,investment_offer_id):
    investment_offer = InvestmentOffer.objects.get(id=investment_offer_id)
    investment_offer.delete()
    return redirect("fund:investment_requests_view")


def negotiate_view(request:HttpRequest,investment_offer_id):
    investment_offer = InvestmentOffer.objects.get(id=investment_offer_id)
    comments = InvestmentOfferComment.objects.filter(investment_offer=investment_offer)
    return render(request,"fund/negotiate.html",{"investment_offer":investment_offer,"comments":comments})


def add_comment_view(request:HttpRequest,investment_offer_id):
        if request.method == "POST":
            investment_offer = InvestmentOffer.objects.get(id =investment_offer_id)
            new_comment = InvestmentOfferComment(investment_offer=investment_offer , user=request.user,content=request.POST["content"])
            new_comment.save()
            return redirect("fund:negotiate_view",investment_offer_id = investment_offer.id)
    



    
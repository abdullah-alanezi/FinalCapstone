from django.db import models
from django.contrib.auth.models import User
#from startup.models import FundingRound

# Create your models here.
class InvestmentOffer(models.Model):
    status = models.TextChoices("status",["Pending","Approved","Disapproved","Canceled"])
    #funding_round = models.ForeignKey(FundingRound,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    percentage = models.FloatField()
    amount = models.IntegerField()
    status = models.CharField(max_length=64,choices=status.choices, default=status.Pending)
    
    
class InvestmentOfferComment(models.Model):
    investment_offer = models.ForeignKey(InvestmentOffer, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    
    
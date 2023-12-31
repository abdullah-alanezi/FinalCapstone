from django.contrib.auth.models import User
from django.db import models

class InvestorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_investor_profile')
    

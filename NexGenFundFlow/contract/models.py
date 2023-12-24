# from django.db import models
# from django.contrib.auth.models import InvestmentOffer
# from django.contrib.auth.models import InverstorProfile
# from django.contrib.auth.models import StrtatupMangaerProfile
# from django.contrib.auth.models import Starup


# class Contract(models.Model):
#     investment_offer = models.OneToOneField(InvestmentOffer, on_delete=models.CASCADE)
#     investor_profile = models.ForeignKey(InvestorProfile, on_delete=models.CASCADE)
#     contract_date = models.CharField(max_length=255)
#     payment_due = models.CharField(max_length=255)
#     startup_manager_profile = models.ForeignKey(StartupManagerProfile, on_delete=models.CASCADE)
#     startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
#     contract_pdf = models.FileField(upload_to='contracts/')

# class ContractPdf(models.Model):
#     contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
#     contract_role = models.TextField()
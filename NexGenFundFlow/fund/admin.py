from django.contrib import admin
from .models import InvestmentOffer , InvestmentOfferComment
# Register your models here.

class InvestmentOfferAdmin(admin.ModelAdmin):
    list_display = ('status','funding_round','user','percentage','amount')
    
class InvestmentOfferCommentAdmin(admin.ModelAdmin):
    list_display =('investment_offer','user','content')
    
admin.site.register(InvestmentOffer, InvestmentOfferAdmin)
admin.site.register(InvestmentOfferComment, InvestmentOfferCommentAdmin)
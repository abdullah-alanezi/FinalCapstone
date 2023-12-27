from . import views
from django.urls import path

app_name = 'fund'


urlpatterns = [
    path("funding/round/",views.all_funding_round_view,name="all_funding_round_view"),
    path("funding/round/details/<funding_round_id>/",views.funding_round_details_view,name="funding_round_details_view"),
    path("investment/requests/",views.investment_requests_view,name="investment_requests_view"),
    path("cancel/investment/offer/<investment_offer_id>/",views.cancel_investment_offer_view,name="cancel_investment_offer_view"),
    
]
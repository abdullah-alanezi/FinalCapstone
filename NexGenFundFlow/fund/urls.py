from . import views
from django.urls import path

app_name = 'fund'


urlpatterns = [
    path("funding/round/",views.all_funding_round_view,name="all_funding_round_view"),
    path("funding/round/details/<funding_round_id>/",views.funding_round_details_view,name="funding_round_details_view"),
    
]
# urls.py في تطبيق contract
from django.urls import path
from . import views

app_name = 'contract'

urlpatterns = [
    path('deal_form/', views.your_form_view, name='deal_form'), 
    path('create-deal-pdf/<int:investment_request_id>/', views.create_deal_pdf, name='create_deal_pdf'),

]

from . import views
from django.urls import path

app_name = 'contract'


urlpatterns = [
        path('deal_form/', views.your_form_view, name='deal_form'),
        path('create-deal-pdf/', views.create_deal_pdf, name='create_deal_pdf'),

]
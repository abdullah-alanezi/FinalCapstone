from . import views
from django.urls import path

app_name = 'home'


urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('404/',views.page_not_found_view,name='page_not_found_view')
]
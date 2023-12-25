
from . import views
from django.urls import path

app_name = 'user'


urlpatterns = [
    path('logup/',views.logup_view,name='logup_view'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
]
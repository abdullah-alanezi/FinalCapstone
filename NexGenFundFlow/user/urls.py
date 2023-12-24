
from . import views
from django.urls import path

app_name = 'user'


urlpatterns = [
    path('logup/',views.logup_view,name='logup_view')
]
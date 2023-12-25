from . import views
from django.urls import path

app_name = 'startup'


urlpatterns = [
    path('create/',views.create_startup_view,name='create_startup_view'),
]
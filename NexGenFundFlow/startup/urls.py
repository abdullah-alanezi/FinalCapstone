from . import views
from django.urls import path

app_name = 'startup'


urlpatterns = [
    path('create/',views.create_startup_view,name='create_startup_view'),
    path('brows/<startup_id>/',views.view_startup_profile_view,name='view_startup_profile_view'),
    path('edit/<startup_id>/',views.edit_startup_view,name='edit_startup_view'),
    path('<startup_id>/team/',views.team_view,name='team_view'),
    path('<startup_id>/add/team/',views.add_team_member_view,name='add_team_member_view'),
    path('all/<user_id>/',views.view_all_my_stratup_view,name='view_all_my_stratup_view'),
]
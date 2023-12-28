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
    path('<startup_id>/funding/create/',views.funding_round_view,name='funding_round_view'),
    path('<startup_id>/all/fund/',views.all_funding_round_view,name='all_funding_round_view'),
    path('view/startup/<startup_id>/requests/',views.view_funding_request,name='view_funding_request'),
    path('<request_id>/approved/request',views.approved_reqeust_view,name='approved_reqeust_view'),
    path('<request_id>/disapproved/request',views.disapproved_reqeust_view,name='disapproved_reqeust_view'),
]
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate , login , logout
from . models import StartupManagerProfile, InvestorProfile

# Create your views here.


def logup_view(request:HttpRequest):
    msg=None
    if request.method == 'POST':
        try:
            
            user = User.objects.create_user(username=request.POST['username'],email = request.POST['email'],password = request.POST['password'])
            user.save()

            user_field = request.POST.get('selected_option')

            if user_field == 'investor':
                
                if not user.groups.filter(name='Investors').exists():
                    group = Group.objects.get(name="Investors")
                    user.groups.add(group)

            elif user_field == 'startup':
                if not user.groups.filter(name='StartupsManagers').exists():
                    group = Group.objects.get(name="StartupsManagers")
                    user.groups.add(group)

            user = authenticate(request, username=request.POST['username'],password=request.POST['password'])

            if user:
                login(request,user)
            
            return redirect('user:profile_view',request.user.id)
       
        except Exception as e:

            msg = e

            if 'UNIQUE constraint failed: auth_user.username' in str(e):
                
                msg ='Username already exists'
            else :
                msg = e

            
    return render(request,'user/logup.html',{'massage':msg})



def login_view(request:HttpRequest):
    msg = None
    if request.method == 'POST':

        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])

        if user:
            login(request,user)
            
            return redirect('home:home_view')
        
        else:
            msg ='please provide correct username and password'

        

    return render(request,'user/login.html',{'massage':msg})


def logout_view(request:HttpRequest):

    if request.user.is_authenticated:

        logout(request)

        return redirect('user:login_view')
    


def profile_view(request:HttpRequest,user_id):
        
        msg = None
        user = User.objects.get(id=user_id)

        startups_managers = User.objects.filter(groups__name ='StartupsManagers')
        
        investors = User.objects.filter(groups__name ='Investors')       

        if request.user in investors:
            try:
                profile = request.user.investorprofile
            except Exception:
                msg = 'Please update your profile'

        elif request.user in startups_managers:

            try:
                s=request.user.startupmanagerprofile
            except Exception:
                msg = 'Please update your profile'



        return render(request,'user/profile.html',{'user':user,'investors':investors,'startups_managers':startups_managers,'massage':msg})


def update_profile_view(request:HttpRequest):

    investors = User.objects.filter(groups__name = 'Investors')

    

    user = User.objects.get(id=request.user.id)

    startups_managers = User.objects.filter(groups__name ='StartupsManagers')

    if request.user.is_authenticated:
        if user in startups_managers:
            if request.method == 'POST':

                user.first_name = request.POST['first_name']
                user.last_name =  request.POST['last_name']
                user.email = request.POST['email']

                user.save()

                try:
                    manager_profile=user.startupmanagerprofile

                except Exception as e:
                        
                    manager_profile = StartupManagerProfile(user=user)

                manager_profile.position = request.POST['position']
                manager_profile.manager_phone_number = request.POST['manager_phone_number']
                manager_profile.manager_birth_day = request.POST['manager_birth_day']
                manager_profile.manager_x_link = request.POST['manager_x_link']
                manager_profile.manager_bio = request.POST['manager_bio']
                manager_profile.manager_city = request.POST['manager_city']
                manager_profile.manager_LinkedIn = request.POST['manager_LinkedIn']
                                                            
                                                            
                if 'manager_avatar' in request.FILES:

                        manager_profile.manager_avatar = request.FILES['manager_avatar']

                manager_profile.save()

                return redirect('user:profile_view',request.user.id)
        
        elif request.user in investors:
            
            if request.method == 'POST':

                user.first_name = request.POST['first_name']
                user.last_name =  request.POST['last_name']
                user.email = request.POST['email']

                user.save()

                try:
                    investor_profile = user.investorprofile
                except Exception as e:
                        
                    investor_profile = InvestorProfile(user=user)

                investor_profile.specialization = request.POST['specialization']
                investor_profile.inverstor_phone_number = request.POST['inverstor_phone_number']
                investor_profile.inverstor_birth_day = request.POST['inverstor_birth_day']
                investor_profile.inverstor_x_link = request.POST['inverstor_x_link']
                investor_profile.inverstor_bio = request.POST['inverstor_bio']
                investor_profile.inverstor_city = request.POST['inverstor_city']
                investor_profile.inverstor_LinkedIn = request.POST['inverstor_LinkedIn']
                                                            
                                                            
                if 'inverstor_avatar' in request.FILES:

                        investor_profile.inverstor_avatar = request.FILES['inverstor_avatar']

                investor_profile.save()

                return redirect('user:profile_view',request.user.id)
    
    context = {
        
        'investors':investors,
        'startups_managers':startups_managers,
        'user':user

    }
                
                        
    return render(request,'user/update_profile.html',context)


def investors_view(request:HttpRequest):

    investors = User.objects.filter(groups__name ='Investors') 

    return render(request,'user/investors.html',{'investors':investors})
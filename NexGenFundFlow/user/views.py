from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate , login , logout
from . models import StartupManagerProfile, InvestorProfile
# Create your views here.


def logup_view(requset:HttpRequest):
    msg=None
    if requset.method == 'POST':
        try:
            
            user = User.objects.create_user(username=requset.POST['username'],first_name = requset.POST['first_name'],last_name=requset.POST['last_name'],email = requset.POST['email'],password = requset.POST['password'])
            user.save()

            user_field = requset.POST.get('selected_option')

            if user_field == 'investor':
                
                if not user.groups.filter(name='Investors').exists():
                    group = Group.objects.get(name="Investors")
                    user.groups.add(group)

            elif user_field == 'startup':
                if not user.groups.filter(name='StartupsManagers').exists():
                    group = Group.objects.get(name="StartupsManagers")
                    user.groups.add(group)
            

            #return profile page
            #return redirect('user:')
        except Exception as e:
            msg = e
    return render(requset,'user/logup.html',{'massage':msg})



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
    


def profile_view(request:HttpRequest):
        
        #user = User.objects.filter(groups__name ='Investors')

        return render(request,'user/profile.html')


def update_profile_view(request:HttpRequest):
    
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
                    manager_profile=request.user.startupmanagerprofile
                except Exception as e:
                        
                    manager_profile = StartupManagerProfile(user=user,

                    position = request.POST['position'],
                    manager_phone_number = request.POST['manager_phone_number'],
                    manager_birth_day = request.POST['manager_birth_day'],
                    manager_x_link = request.POST['manager_x_link'],
                    manager_bio = request.POST['manager_bio'],
                    manager_city = request.POST['manager_city'],
                    manager_LinkedIn = request.POST['manager_LinkedIn']
                                                            
                                                            )
                    if 'manager_avatar' in request.method:

                        manager_profile.manager_avatar = request.FILES['manager_avatar']

                    manager_profile.save()
        else:
            return redirect('home:home_view')
                
                        
    return render(request,'user/update_profile.html')
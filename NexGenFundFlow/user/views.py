from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate , login , logout
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

            #return login page
            #return redirect('login page:')
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
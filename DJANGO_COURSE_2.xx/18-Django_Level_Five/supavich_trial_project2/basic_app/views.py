from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
# Create your views here.
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request,"basic_app/index.html")

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user
            
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
                
            profile.save()
            
            registered = True
        else:
            print("Error")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
        
    return render(request,"basic_app/registration.html",
                  {"registered":registered,
                   "user_form":user_form,
                   "profile_form":profile_form
                                   
                  })
    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username,password = password)
        #user return
        if user:
            if user.is_active:
                login(request,user)
                print("Log in successful")
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not Active")
        else:
            print("Someone try to access account with")
            print("Username:{} Password{}".format(username,password))
            
            return HttpResponse("Invalid login details supplied")
            
    return render(request,"basic_app/login.html",{})
    
            
        
from django.shortcuts import render
from basic_app.models import UserProfileInfo
from basic_app.forms import UserForm,UserProfileInfoForm
# Create your views here.

from django.urls import reverse
from django.contrib.auth.decorators import login_required
#this allow the user required to log in to be able access content.
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout



def index(request):
    return render(request,"basic_app/index.html")

@login_required
def special(request):
    return HttpResponse("You are logged in!Nice")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    

def user_login(request):
    print("hello")
    if request.method == "POST":
        username = request.POST.get("username")
        #this is is use to get from input tag.
        password = request.POST.get("password")
        
        user = authenticate(username = username,password = password)
        #this will authenticate user for you
        print("hello world")
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            
            else:
                return HttpResponse("Account not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username:{} and password {}".format(username,password))
            
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,"basic_app/login.html",{})
        
    
    
def register(request):
    
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)#this hash the password
            user.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user #we link a profile to the user form.
            
            #This is check for all types of files, and the name(profile_pic) will depend on models.py form created.
            if "profile_pic" in request.FILES:
                #request.FILES is a dictionary for all the files upload in the request.
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            
            registered = True
        
           
            
            
        
        else:
            print(user_form.errors,profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request,"basic_app/registration.html",
                  {"registered":registered,
                   "user_form":user_form,
                   "profile_form":profile_form}) 
        
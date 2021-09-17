from django.shortcuts import render
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic import CreateView
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #this mean after they successfully sign up they will be redirect to login page.reverse_lazy and so we can use the url name
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
    

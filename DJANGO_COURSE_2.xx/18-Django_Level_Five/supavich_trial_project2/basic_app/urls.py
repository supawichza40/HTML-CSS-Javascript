from django.contrib import admin
from django.urls import path,include
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    
    path("register/",views.registration,name = "register"),
    path("login/",views.user_login,name = "login"),
    path("logout/",views.log_out,name = "logout"),
]

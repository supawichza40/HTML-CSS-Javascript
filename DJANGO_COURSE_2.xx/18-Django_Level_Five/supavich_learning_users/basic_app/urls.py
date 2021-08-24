from django.contrib import admin
from django.urls import path,include
from basic_app import views

app_name = "basic_app"
urlpatterns = [

    path("register/",views.register,name = "registration"),
    path("login/",views.login,name = "login"),
    path("user_login/",views.user_login,name = "user_login")
]

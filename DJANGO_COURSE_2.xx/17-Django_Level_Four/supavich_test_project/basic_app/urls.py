from django.contrib import admin
from django.urls import path,include
from basic_app import views


#Template Tagging, django will automatic looking for this.
app_name ="basic_app"
#look under the basic app and look if the url match

urlpatterns = [
    path("relative/",views.relative,name = "relative"),
    path("other/",views.other,name = "other"),
    
    
]
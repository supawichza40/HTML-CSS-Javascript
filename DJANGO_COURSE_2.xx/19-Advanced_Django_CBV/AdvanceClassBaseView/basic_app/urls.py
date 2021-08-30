from django.contrib import admin
from django.urls import path,include
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path("",views.SchoolListView.as_view(),name = "list"),
    path("<int:pk>/",views.SchoolDetailView.as_view(),name = "detail"),
    path("create/",views.SchoolCreateView.as_view(),name = "create"),
    path("update/<int:pk>/",views.SchoolUpdateView.as_view(),name = "update"),
    #add update extension to the primary key
    path("delete/<int:pk>/",views.SchoolDeleteView.as_view(),name = "delete")
    
    # the path with pk will require a primary key.
    # by using pk = <object>.pk to get the primary key
]

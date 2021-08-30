from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from basic_app.models import School,Student
from django.urls import reverse_lazy
#For CBV with CRUD design
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
def index(request):
    return render(request,"index.html")

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL! ")

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self,**kwargs):
        #
        context = super().get_context_data(**kwargs)
        context["injectme"] = "This got injected"
        context["injectme2"] = "I just got injected again"
        
        return context
    
class SchoolListView(ListView):
    context_object_name = "schools"
    model = School
    #this will provide a list of information in school.
    #school_list
    
    
class SchoolDetailView(DetailView):
    context_object_name = "school_details"
    model = School
    template_name = "basic_app/school_detail.html"
    
#this class will use the C FROM CRUD to make it easier
#to create new school.
class SchoolCreateView(CreateView):
    model = School
    fields = ("name","principal","location")
    
class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = School
    
class SchoolDeleteView(DeleteView):

    model = School
    success_url = reverse_lazy("basic_app:list")
    #once you finish deleting the school I want you to go to basic_app:list
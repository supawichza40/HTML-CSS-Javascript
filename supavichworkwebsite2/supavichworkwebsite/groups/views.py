from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
# Create your views here.
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from braces.views import SelectRelatedMixin
from groups import models
from django.shortcuts import redirect
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields =("name","description")
    model = Group
    template_name = "groups/group_form.html"
    success_url =  reverse_lazy("groups:all")
    # the reverse_lay is use for name create for the urls.py and we can use it to redirect anywhere we want using its name
class SingleGroup(generic.DetailView):
    model = Group
    
class ListGroups(generic.ListView):
    model = Group
    context_object_name = "all_groups"
    # the original name is object_list
    template_name = "groups/group_list.html"
    
class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):

        print("I am in join group")
        return reverse("groups:single",kwargs={"slug":self.kwargs.get("slug")})
    
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))
        
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
            
        except IntegrityError:
            messages.warning(self.request, "Warning already a member")
        else:
            
            messages.success(self.request, "You are now a member")
            
        return super().get(request,*args,*kwargs)
    

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        print("I am in leave group")
        return reverse("groups:single",kwargs={"slug":self.kwargs.get("slug")})
    
    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
                
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, "Sorry you are not in this group")
            
        else:
            membership.delete()
            messages.success(self.request,"You have left the group!")
        return super().get(request,*args,**kwargs)
    
# class DeleteGroup(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
#     model = models.Group
#     select_related = ("name","description")
#     success_url = reverse_lazy("groups:all")
    
#     def delete(self, *args, **kwargs):
#         messages.success(self.request, "Group Deleted")
#         return super().delete(*args, **kwargs)
        
    
def delete_group(request,pk):
    if request.method == "POST":
        group = Group.objects.get(pk=pk)
        group.delete()
        return redirect("groups:all")
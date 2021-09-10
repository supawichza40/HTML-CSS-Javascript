from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
from blog.models import Post,Comment
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
#for class base view
from django.contrib.auth.decorators import login_required 
#for function base view
from blog.forms import PostForm,CommentForm

#this prevent to go to another page before successfully delete.
from django.urls import reverse_lazy
class AboutView(TemplateView):
    template_name = "about.html"
    
class PostListView(ListView):
    model = Post
    #this is for filtering information and arrange in order.
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date") 
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    #This is required for the mixin
    form_class = PostForm
    model = Post
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    #in case if the person not log in where they go
    
    redirect_field_name = "blog/post_detail.html"
    #after they complete, where should they go.
    form_class = PostForm
    model = Post
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")
    
class DraftListView(LoginRequiredMixin,ListView):
    login_url = "/login/"
    redirect_field_name = "blog/post_draft_list.html"
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("created_date")
    
#############################
##############################
##############################
from django.shortcuts import get_object_or_404,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            #we are creating a new comment object since, we
            #do not want to change form but want to add post
            #to the form without changing it.
            comment = form.save(commit = False)
            comment.post = post
            #this directly comment to model foreign key blog.post
            comment.save()
            return redirect("post_detail",pk = post.pk)#since post_detail require a pk.
    else:
        form = CommentForm()
    return render(request,"blog/comment_form.html",{"form":form})#this is related to else statement only.


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect("post_detail",pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk =pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("post_detail",pk = post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect("post_detail",pk=pk)
    
    
        
    
    
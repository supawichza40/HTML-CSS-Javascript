from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()
#this connect the current post to whoever log in as a current users

# Create your models here.
# Post models.py

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    #auto generate time it posts
    message = models.TextField()
    message_html = models.TextField(editable=False)
    work_files = models.FileField(upload_to="works_folder",blank = True)
    group = models.ForeignKey(Group,related_name='posts',null = True,blank= True,on_delete=models.CASCADE)
    
    def  __str__(self):
        return self.user.name
    
    def save(self,*args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        print("I am in the post single and will redirect you!")
        return reverse("posts:single",kwargs={"username":self.user.username,
                                              "pk":self.pk})
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user","message"]
        
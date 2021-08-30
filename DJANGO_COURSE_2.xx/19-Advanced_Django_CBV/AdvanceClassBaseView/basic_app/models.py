from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)
    def get_absolute_url(self):
        #go back in reverse to the detail page of what the new school you just created.
        return reverse("basic_app:detail",kwargs = {"pk":self.pk})
        
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete = models.CASCADE, related_name = "students")
    #related name allow us to call it.
    def __str__(self):
        return self.name
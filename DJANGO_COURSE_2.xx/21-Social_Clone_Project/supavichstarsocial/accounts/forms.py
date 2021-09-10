from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username","email","password1","password2")
        # for confirming password
        model = get_user_model()
        
        
# this is for personal customization of the form        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].label = "Display Name"
        #this is for label in the form instead of it name
        self.fields["email"].label = "Email Address"
        
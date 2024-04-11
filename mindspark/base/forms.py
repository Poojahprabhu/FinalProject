from django.forms import ModelForm
from .models import user, feedback 

class userForm(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'usn', 'dob', 'gender', 'disability', 'sem', 'college', 'username', 'password', 'email', 'phone']


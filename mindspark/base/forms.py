from django.forms import ModelForm
from .models import user, feedback  

class userForm(ModelForm):
    class Meta:
        model = user
        fields = "__all__"

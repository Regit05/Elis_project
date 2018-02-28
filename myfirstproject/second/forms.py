from django.forms import ModelForm
from .models import User_custom

class UserForm(ModelForm):
    class Meta:
        model = User_custom
        fields = ['pseudo', 'mdp']
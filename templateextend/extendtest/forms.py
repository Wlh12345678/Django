from django import forms
from .models import User

# class CustomForm(forms.Form):
#     title = forms.CharField()
#     datetime =

class CustomForm(forms.ModelForm):
    class meta():
        model = User
        fields = ['username','password']



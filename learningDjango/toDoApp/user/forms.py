from django import forms

class Create_user_form(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    Email = forms.EmailField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True)
    
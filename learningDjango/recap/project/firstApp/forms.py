from django import forms
from firstApp.models import ContactModel

class CreateContactForm(forms.Form):
    user_name = forms.CharField(max_length=100, min_length=5, required=True)
    phone = forms.CharField(max_length=15, min_length=5, required=True)
    user_age = forms.IntegerField() 
    user_email = forms.EmailField(max_length=100, min_length=10, required=True)
    address = forms.CharField(max_length=100, min_length=20, required=False)

class CreateContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'phone', 'email']

    
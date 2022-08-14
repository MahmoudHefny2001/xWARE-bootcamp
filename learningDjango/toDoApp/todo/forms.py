from django import forms

class Create_task_form(forms.Form):
    name = forms.CharField(max_length=200, required=True)


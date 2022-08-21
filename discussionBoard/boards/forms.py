from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    
    essay = forms.CharField(
                widget = forms.Textarea(attrs= {'rows': 8, 'placeholder': 'What\'s in your mind?'}),
                max_length = 5000,
                help_text = 'Maximum length of the text is 5000 '
               )
    
    class Meta:
        model = Topic
        fields = ['topic', 'essay']

    
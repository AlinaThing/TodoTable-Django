from django import forms
from .models import TodoItems

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['text', 'name', 'start_date', 'completion_date', 'is_completed']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Enter your new TODO'}),
            'name': forms.TextInput(attrs={'placeholder': 'Assigned BY'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Start Date'}),
            'completion_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Completion Date'}),
            'is_completed': forms.CheckboxInput(),
        }



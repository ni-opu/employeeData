from django.core import validators
from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'employee_id', 'shift', 'arrival', 'remark']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'shift': forms.Select(attrs={'class': 'form-select'}),
            'arrival': forms.Select(attrs={'class': 'form-select'}),
            'remark': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
        }
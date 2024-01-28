from django import forms
from .models import Form

class FormModelForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            # 'delivery_period': forms.DateInput(attrs={'type': 'date'}),
        }

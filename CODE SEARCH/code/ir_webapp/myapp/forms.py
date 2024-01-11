# myapp/forms.py
from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['text_input']
        widgets = {
            'text_input': forms.TextInput(attrs={'class': 'border p-2 w-full'}),
        }

from django import forms
from .models import master_table

class empforms(forms.ModelForm):
    class Meta:
        model=master_table
        fields="__all__"
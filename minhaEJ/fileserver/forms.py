from django import forms
from .models import *

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ["nome", "email","cargo", "status"]
from django import forms

from .models import File

# Class que representa o formulário de upload de arquivos
# O atributo 'widgets' foi inserido pq alguns dos campos são preenchidos, automaticamente
# com informações do próprio arquivo informado pelo usuário. Esse campos são preenchidos no
# controller que controla a view de uploads
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'size', 'location', 'owner')
        widgets = {'name': forms.HiddenInput(), 'size': forms.HiddenInput(), 'owner': forms.HiddenInput()}
        labels = {'location': 'Arquivo'}

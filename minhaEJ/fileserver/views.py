from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


def home(request):  
    return render(request, 'fileserver/home.html')

def about(request):
    return render(request, 'fileserver/about.html', {'title': 'About'})



def cadastrar_usuario(request):      
    form = MembroForm(request.POST)
    if form.is_valid():
        salvar = form.save(commit=False)
        salvar.save()
        return render(request, 'fileserver/cadastro_membro_sucesso.html')
    
    return render(request, "fileserver/membros.html", {'form':form})


class Lista(ListView):
        template_name = 'membros.html'
        model = Membro
        context_object = 'nome'
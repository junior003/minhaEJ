from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from users import *
from fileserver.models import Membro
from fileserver.forms import MembroForm

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



class MembroListView(ListView):
    template_name = "fileserver/listamembros.html"
    model = Membro
    context_object_name = "Membros"
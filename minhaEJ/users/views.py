from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Função responsável por cadastrar o usuário no BD
def register(request):
    if request.method == 'POST':        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Sua conta foi criada! Já pode realizar seu login se quiser.')
            
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

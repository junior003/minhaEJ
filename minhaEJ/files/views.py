from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import FileForm
from .models import File

# Apenas usuários logados podem ser acessar a página que lista os arquivos enviados
@login_required(login_url='/login/')
# Função responsável por exibir a página que lista os arquivos enviados pelo usuário
# atualmente conectado ao sistema. Apesar de estar localizado num arquivo chamado view.py,
# representa o Controller que chama a View (o template, no caso do Django) adequada
def file_list(request):
    files = File.objects.filter(owner=request.user)
    number_of_files = files.count()
    return render(request, 'files/file_list.html', {
        'files': files,
        'number_of_files': number_of_files
    })

# Apenas usuários logados podem ser acessar a página para upload de arquivos
@login_required(login_url='/login/')
# Função responsável por exibir a página na qual os usuários enviarão seus arquivos
def upload_file(request):
    user_id = request.user.id    
    
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        uploaded_file = request.FILES['location']
        
        if form.is_valid():
            form_aux = form.save(commit=False)
            form_aux.owner = request.user
            form_aux.name = uploaded_file.name
            form_aux.size = uploaded_file.size
            form_aux.save()
            
            return redirect('file_list')
    else:
        form = FileForm()
    
    return render(request, 'files/upload_file.html', {
        'form': form
    })

# Apenas usuários logados podem ser acessar a página de remoção de arquivos
@login_required(login_url='/login/')
# Função responsável por realizar a remoção do registro do arquivo no banco de dados,
# bem como na unidade de armazenamento 
def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(id=pk)
        file.delete()
        
    return redirect('file_list')

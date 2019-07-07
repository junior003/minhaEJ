from django.shortcuts import render
from django.http import HttpResponse

def home(request):  
    return render(request, 'fileserver/home.html')

def about(request):
    return render(request, 'fileserver/about.html', {'title': 'About'})

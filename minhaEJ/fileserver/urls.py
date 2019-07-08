from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fileserver-home'),
    path('membros/', views.cadastrar_usuario, name='cadastrar_usuario'),
    
] 

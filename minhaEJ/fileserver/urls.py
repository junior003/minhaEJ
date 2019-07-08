from django.urls import path
from . import views
from fileserver.views import MembroListView
from django.views.generic import TemplateView




urlpatterns = [
    path('', views.home, name='fileserver-home'),
    path('membros/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('listamembros/', MembroListView.as_view(), name="lista_membros"),


] 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fileserver-home'),
    path('about/', views.about, name='fileserver-about'),
] 

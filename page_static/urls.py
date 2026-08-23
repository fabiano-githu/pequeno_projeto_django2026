from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('sobre/', views.sobre, name='sobre'),

    path('contatos/', views.contatos, name='contatos'),

    path('servicos/', views.servicos, name='servicos'),

   path('certificados/', views.certificados, name='certificados'),

]
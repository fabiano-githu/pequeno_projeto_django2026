
# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'page_static/home.html')


def contatos(request):
    return render(request, 'page_static/contatos.html')


def sobre(request):
    return render(request, 'page_static/sobre.html')


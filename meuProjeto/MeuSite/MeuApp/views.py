from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Olá, mundo! Esta é a página inicial do MeuApp.", content_type="text/plain")
    return render(request, "MeuApp/home.html")

def segundaPagina(request):
    return render(request, "MeuApp/segundaPagina.html")
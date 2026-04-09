from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

def home(request):
    #return HttpResponse("Olá, mundo! Esta é a página inicial do MeuApp.", content_type="text/plain")
    agora = timezone.localtime()

    if agora.hour < 12:
        saudacao = "Bom dia"
    elif agora.hour < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    nome_usuario = request.user.username if request.user.is_authenticated else "visitante"

    contexto = {
        "saudacao": saudacao,
        "nome_usuario": nome_usuario,
        "horario": agora.strftime("%H:%M:%S"),
    }

    return render(request, "MeuApp/home.html", contexto)

def segundaPagina(request):
    return render(request, "MeuApp/segundaPagina.html")
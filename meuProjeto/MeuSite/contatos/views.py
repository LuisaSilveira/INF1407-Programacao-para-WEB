from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic.base import View
from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic.base import View
from contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(
            request,
            'contatos/listaContatos.html',
            contexto)
    
class ContatoCreateView(View):
    def get(self, request):
        contexto = {'formulario': ContatoModel2Form()}
        return render(request, 'contatos/criaContatos.html', contexto)
    
    def post(self, request):
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        else:
            contexto = {'formulario': formulario}
            return render(request, 'contatos/criaContatos.html', contexto)
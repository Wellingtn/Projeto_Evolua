from django.shortcuts import render
from cadastro.models import cadastro

def cadastro(request):
    return render(request, "reqcadastro/cadastro.html")

def cadastros (request):
    novo_usuario = cadastro
    novo_usuario.id = request.POST.get('id')
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.nascimento = request.POST.get('nascimento')
    novo_usuario.save()
    
    return render(request )
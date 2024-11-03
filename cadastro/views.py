from django.shortcuts import render

def cadastro(request):
    return render(request, "reqcadastro/cadastro.html")
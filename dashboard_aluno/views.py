from django.shortcuts import render

def dashboard_aluno(request):
    return render(request, "reqaluno/aluno.html")

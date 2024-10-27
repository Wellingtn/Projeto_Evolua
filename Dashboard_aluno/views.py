from django.shortcuts import render

def dashboard_aluno(request):
    return render(request, 'Dashboard_aluno/dash_aluno.html')

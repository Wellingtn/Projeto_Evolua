from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def login(request):
    template_name = 'reqlogin/login.html'
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user=authenticate(request, email=email, senha = senha)

        if user is not None:
            # and user == 'professor :
            login(request, user)
            return redirect('dashboard_prof/views.py')


    return render(request, template_name)

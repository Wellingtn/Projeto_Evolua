from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login(request):
    template_name = 'reqlogin/login.html'
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user=authenticate(request, username=email, senha = senha)

        if user is not None:
            
            login(request, user)
            return redirect('dashboard_prof:templates:professor.html')
        
        else:
            return render(request, template_name, {'error': 'Credenciais inválidas'})

            

    return render(request, template_name)




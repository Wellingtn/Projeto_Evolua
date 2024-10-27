from django.shortcuts import render

def dashboard_prof(request):
    return render(request, 'Dashboard_prof/dash_prof.html')

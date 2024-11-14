from django.shortcuts import render, redirect

def quiz(request):
    
    template_name="reqquiz/quiz.html"

    
    
    
    return render(request, template_name)

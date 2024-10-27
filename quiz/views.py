from django.shortcuts import render

def quiz(request):
    return render(request, "quizzes/quiz.html")
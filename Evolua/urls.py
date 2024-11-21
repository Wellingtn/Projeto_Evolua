from django.contrib import admin
from django.urls import path, include

from login.views import login
from dashboard_aluno.views import dashboard_aluno
from dashboard_prof.views import dashprof
from quiz.views import quiz
from cadastro.views import cadastro

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login, name="login"), 
    path("dashboard_aluno/", dashboard_aluno, name="dashboard_aluno"),
    path("dashboard_prof/", dashprof, name="dashboard_prof"),
    path("quiz/", quiz, name="quiz"),
    path("cadastro/", cadastro, name="cadastro"), 
]
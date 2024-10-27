from django.contrib import admin
from django.urls import path

from login.views import login
from dashboard_aluno.views import dashboard_aluno
from dashboard_prof.views import dashprof
from quiz.views import quiz

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login), 
    path("dashboard_aluno/", dashboard_aluno),
    path("dashboard_prof/", dashprof),
    path("quiz/", quiz),


]

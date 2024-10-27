from django.contrib import admin
from django.urls import path
from Login.views import Login
from Dashboard_aluno.views import dashboard_aluno
from Dashboard_prof.views import dashboard_prof
from quiz.views import quiz

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Login), 
    path("/0", dashboard_aluno),
    path("/1", dashboard_prof),
    path("/2", quiz),


]

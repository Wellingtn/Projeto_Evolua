from django.contrib import admin
from django.urls import path
from Login.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login),
]

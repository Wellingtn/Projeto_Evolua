from django.db import models

class Login(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    nascimento = models.DateField(auto_now_add=True, null=False, blank=False)

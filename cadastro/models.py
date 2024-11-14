from django.db import models

class cadastro(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    nome = models.TextField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    nascimento = models.DateField(auto_now_add=True, null=False, blank=False)

    def _self_ (    ):
        return self
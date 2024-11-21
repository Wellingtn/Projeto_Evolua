from django.db import models

class Pilar(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    pontos = models.IntegerField()
    porcentagem = models.DecimalField(max_digits=5, decimal_places=2)
    nivel = models.CharField(max_length=50)

    def _str_(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    semestre = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)
    desempenho = models.ManyToManyField(Pilar, through='DesempenhoAluno')

    def _str_(self):
        return self.nome

class DesempenhoAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    pilar = models.ForeignKey(Pilar, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()



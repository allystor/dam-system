from django.db import models

# Create your models here.
class TipoBacia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Engenheiro(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    crea = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Bacia(models.Model):
    tipoBacia = models.ForeignKey(TipoBacia, on_delete=models.CASCADE)
    profundidade = models.FloatField(null=False, blank=True)
    capacidade = models.FloatField(null=False, blank=True)
    largura = models.FloatField(null=False, blank=True)
    comprimento = models.FloatField(null=False, blank=True)
    engenheiro = models.ForeignKey(Engenheiro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    numero = models.IntegerField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return self.nome
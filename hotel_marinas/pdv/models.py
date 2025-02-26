from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome
    
class Quarto(models.Model):
    numero = models.CharField(max_length=3)
    tipo   = models.CharField(max_length= 100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete= models.CASCADE)
    data_ent = models.DateTimeField()
    data_sai = models.DateTimeField()

    def __str__(self):
            return self.nome


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_desp = models.DateTimeField()

    def __str__(self):
        return self.nome

class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_rec = models.DateTimeField()

    def __str__(self):
        return self.nome


    def __str__(self):
        return f"{self.descricao} - {self.valor} em {self.data_rec}"

    




from django.db import models

class revenues(models.Model):
    descricao = models.CharField(max_length=100, null=False)
    valor = models.CharField(max_length=10, null=False)
    data = models.DateField()

    def __str__(self):
        return self.descricao
    
class expenses(models.Model):
    descricao = models.CharField(max_length=100, null=False)
    valor = models.CharField(max_length=10, null=False)
    data = models.DateField()

    def __str__(self):
        return self.descricao
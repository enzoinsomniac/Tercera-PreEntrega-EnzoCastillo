from django.db import models

# Create your models here.
class Guitarra(models.Model):
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)

class Provedor(models.Model):
    nombre = models.CharField(max_length=30)
    

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)



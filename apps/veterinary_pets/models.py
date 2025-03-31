from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

# Create your models here.
class Mascota(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    nombre_mascota = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    edad = models.IntegerField()
    sintomas = models.TextField()
    foto = models.ImageField(upload_to='mascotas/', null=True, blank=True)

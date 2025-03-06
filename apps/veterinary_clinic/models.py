from django.db import models

# Create your models here.
class HistoriaClinica(models.Model):
    ESPECIES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]

    nombre_mascota = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIES)
    raza = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField()
    duenio = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=15)
    motivo_consulta = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    tratamiento = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_mascota} ({self.dueño})"
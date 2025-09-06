from djongo import models
from bson import ObjectId


class HistoriaClinica(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    nombre_mascota = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, null=True, blank=True, default='Desconocida')
    edad = models.IntegerField()
    duenio = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    motivo_consulta = models.TextField()

    class Meta:
        managed = False  # 🔹 Desactiva migraciones
        db_table = "veterinary_clinic_historiaclinica"
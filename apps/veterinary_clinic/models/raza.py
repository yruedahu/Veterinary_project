from djongo import models
from bson import ObjectId
from .especie import Especie

class Raza(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    nombre = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

    class Meta:
        db_table = "razas"

    def __str__(self):
        return f"{self.nombre} ({self.especie.nombre})"
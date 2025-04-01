from djongo import models
from bson import ObjectId
from .departamento import Departamento

class Ciudad(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        db_table = "ciudades"

    def __str__(self):
        return f"{self.nombre} ({self.departamento.nombre})"

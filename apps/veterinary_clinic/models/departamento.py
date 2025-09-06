from djongo import models
from bson import ObjectId

class Departamento(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "departamentos"

    def __str__(self):
        return self.nombre

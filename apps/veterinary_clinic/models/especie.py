from djongo import models
from bson import ObjectId

class Especie(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "especies"

    def __str__(self):
        return self.nombre
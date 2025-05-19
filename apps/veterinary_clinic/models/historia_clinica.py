from djongo import models
from bson import ObjectId
from .departamento import Departamento
from .ciudad import Ciudad
from .especie import Especie
from .raza import Raza
from django.utils import timezone

class HistoriaClinica(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    nombre_mascota = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.SET_NULL, null=True)
    raza = models.ForeignKey(Raza, on_delete=models.SET_NULL, null=True)
    edad = models.IntegerField()
    duenio = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)
    motivo_consulta = models.TextField()
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    fecha_atencion = models.DateTimeField(default=timezone.now)
    diagnostico = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "historias_clinicas"

    def __str__(self):
        return f"{self.nombre_mascota} - {self.fecha_atencion}"
    
    @property
    def id_str(self):
        return str(self._id)

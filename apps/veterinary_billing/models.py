from djongo import models

class Producto(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100)
    detalle = models.TextField()
    precio_unitario = models.FloatField()

    def __str__(self):
        return f"{self.nombre} - ${self.precio_unitario}"

class ProductoEmbebido(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField()
    precio_unitario = models.FloatField()

    class Meta:
        abstract = True

class Factura(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    tipo_mascota = models.CharField(max_length=50)
    nombre_mascota = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    productos = models.ArrayField(
        model_container=ProductoEmbebido,
        null=True,
        blank=True
    )
    precio_total = models.FloatField()

    def __str__(self):
        return f'Factura de {self.nombre_cliente} - {self.identificacion}'

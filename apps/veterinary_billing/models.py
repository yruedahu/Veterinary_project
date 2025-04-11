from django.db import models

class Factura(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    mascota = models.CharField(max_length=100)
    servicio = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Factura - {self.nombre_cliente} - {self.mascota}"

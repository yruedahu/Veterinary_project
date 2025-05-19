from django.db import models


class Accesorios(models.Model):  #Esta heredando de models.model
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True) # aqui va el link de la imagen que aparece en el front

    def __str__(self):
        return f"{self.nombre}"


class Medicamentos(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True) # aqui va el link de la imagen que aparece en el front

    def __str__(self):
        return f"{self.nombre}"


class Proveedores(models.Model): 
    TIPO_SERVICIO_CHOICES = [
        ('Alimento', 'Alimento'),
        ('Accesorios', 'Accesorios'),
        ('Cuidado e Higiene', 'Cuidado e Higiene'),
        ('Juguetes', 'Juguetes'),
        ('Medicamentos', 'Medicamentos'),
        ('Otros', 'Otros'),
    ]
    TIPO_ESTADO = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    servicio_producto = models.CharField(max_length=100, choices=TIPO_SERVICIO_CHOICES)
    contacto = models.IntegerField(default=0)
    ubicacion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=100, choices=TIPO_ESTADO)

    def __str__(self):
        return f"{self.nombre}"

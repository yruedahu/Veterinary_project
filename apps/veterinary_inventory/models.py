from django.db import models


class Producto(models.Model):  # Asegúrate de que hereda de models.Model
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"


class Proveedor(models.Model): # Con este sabemos de donde vienen los productos
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"


class Cliente(models.Model): #identifica los compradores
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"

class Venta(models.Model): #Registra las compras de los clientes
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente}"

class DetalleVenta(models.Model): #Cuales productos se vendieron y en que cantidad
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.FloatField()

    def __str__(self):
        return f"{self.venta}"
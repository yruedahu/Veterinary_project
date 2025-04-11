from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm  # Importamos el formulario
from django.shortcuts import render, get_object_or_404

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    context = {
        'nombre': producto.nombre,
        'cantidad': producto.cantidad,
        'precio': producto.precio,
        'descripcion': producto.descripcion
    }
    return render(request, 'veterinary_inventory/detalle_producto.html', context) # Esto es para que nos envie a la direccion que necesitamos por id y nos mueste los datos 

def inventory_home(request):
    productos = Producto.objects.all()  # Aquí es donde ocurre el error
    return render(request, 'veterinary_inventory/inventory.html', {'productos': productos})

def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_home')  # Redirigir al inventario
    else:
        form = ProductoForm()
    return render(request, 'veterinary_inventory/agregar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('inventory_home')

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('inventory_home')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'veterinary_inventory/editar_producto.html', {'form': form})

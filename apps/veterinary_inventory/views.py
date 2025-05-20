from django.shortcuts import render, redirect
from .models import Accesorios, Proveedores, Medicamentos # Importar el modelo
from .forms import AccesoriosForm, ProveedoresForm, MedicamentosForm # Importamos el formulario
from django.http import HttpResponse
from openpyxl import Workbook
from bson.decimal128 import Decimal128
from django.shortcuts import render, get_object_or_404
from itertools import chain
from operator import attrgetter


# pylint: disable=no-member

def inventory_home(request):
    query = request.GET.get('q', '')
    tipo = request.GET.get('tipo', '')

    accesorios = Accesorios.objects.all()
    medicamentos = Medicamentos.objects.all()

    if query:
        accesorios = accesorios.filter(nombre__icontains=query)
        medicamentos = medicamentos.filter(nombre__icontains=query)

    if tipo == 'Accesorio':
        medicamentos = []
    elif tipo == 'Medicamento':
        accesorios = []

    return render(request, 'inventory.html', {
        'accesorios': accesorios,
        'medicamentos': medicamentos,
        'query': query,
        'tipo': tipo
    })

#----------------------------------------------------------------------------------------------------------------------------------------
#INICIO ACCESORIOS

def detalle_accesorios(request):
    accesorios = Accesorios.objects.all()
    context = {
        'accesorios': accesorios
    }
    return render(request, 'veterinary_inventory/detalle_accesorios.html', context)

def agregar_accesorios(request):
    if request.method == "POST":
        form = AccesoriosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_home')  # Redirigir al inventario
    else:
        form = AccesoriosForm()
    return render(request, 'veterinary_inventory/agregar_accesorios.html', {'form': form})


def eliminar_accesorios(request, accesorios_id):
    accesorios = Accesorios.objects.get(id=accesorios_id)
    accesorios.delete()
    return redirect('inventory_home')

def editar_accesorios(request, accesorios_id):
    accesorios = Accesorios.objects.get(id=accesorios_id)
    if request.method == "POST":
        form = AccesoriosForm(request.POST, instance=accesorios)
        if form.is_valid():
            form.save()
            return redirect('inventory_home')
    else:
        form = AccesoriosForm(instance=accesorios)
    return render(request, 'veterinary_inventory/editar_accesorios.html', {'form': form})
#FIN ACCESORIOS
#----------------------------------------------------------------------------------------------------------------------------------------
#INICIO PROVEEDOR
def inventory_home2(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'inventory.html', {'proveedores': proveedores} )

def detalle_proveedores(request):
    proveedores = Proveedores.objects.all()
    context = {
        'proveedores': proveedores
    }
    return render(request, 'veterinary_inventory/detalle_proveedores.html', context)

def agregar_proveedores(request):
    if request.method == "POST":
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_home2')  # Redirigir al inventario
    else:
        form = ProveedoresForm()
    return render(request, 'veterinary_inventory/agregar_proveedores.html', {'form': form})

def eliminar_proveedores(request, proveedor_id):
    proveedor = get_object_or_404(Proveedores, id=proveedor_id)
    proveedor.delete()
    return redirect('inventory_home2')

def editar_proveedores(request, proveedor_id):
    proveedor = get_object_or_404(Proveedores, id=proveedor_id)

    if request.method == "POST":
        form = ProveedoresForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('inventory_home2')
    else:
        form = ProveedoresForm(instance=proveedor)

    return render(request, 'veterinary_inventory/editar_proveedores.html', {'form': form})

#FIN PROVEEDORES
#----------------------------------------------------------------------------------------------------------------------------------------

#MEDICINA


def detalle_medicamentos(request):
    medicamentos = Medicamentos.objects.all()
    context = {
        'medicamentos': medicamentos
    }
    return render (request, 'veterinary_inventory/detalle_medicamentos.html', context)

def agregar_medicamentos(request):
    if request.method == "POST":
        form = MedicamentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalle_medicamentos')  # Redirigir a medicamentos
    else:
        form = MedicamentosForm()
    return render(request, 'veterinary_inventory/agregar_medicamentos.html', {'form': form})

def eliminar_medicamentos(request, medicamentos_id):
    medicamentos = Medicamentos.objects.get(id=medicamentos_id)
    medicamentos.delete()
    return redirect('inventory_home')

def editar_medicamentos(request, medicamentos_id):
    medicamentos = Medicamentos.objects.get(id=medicamentos_id)
    if request.method == "POST":
        form = MedicamentosForm(request.POST, instance=medicamentos)
        if form.is_valid():
            form.save()
            return redirect('inventory_home') #redireciona a el home de inventario 
    else:
        form = AccesoriosForm(instance=medicamentos)
    return render(request, 'veterinary_inventory/editar_medicamentos.html', {'form': form})



#INVENTARIO EXCEL 
def exportar_inventario(request):
    wb = Workbook()
    ws = wb.active
    ws.title = "Inventario"

    # Encabezados
    ws.append(["Tipo", "Nombre", "Precio", "Cantidad", "Descripción"])

    # Accesorios
    for accesorio in Accesorios.objects.all():
        ws.append([
            "Accesorio",
            accesorio.nombre,
            float(accesorio.precio.to_decimal()) if isinstance(accesorio.precio, Decimal128) else accesorio.precio,
            int(accesorio.cantidad.to_decimal()) if isinstance(accesorio.cantidad, Decimal128) else accesorio.cantidad,
            accesorio.descripcion
        ])

    # Medicamentos
    for medicamento in Medicamentos.objects.all():
        ws.append([
            "Medicamento",
            medicamento.nombre,
            float(medicamento.precio.to_decimal()) if isinstance(medicamento.precio, Decimal128) else medicamento.precio,
            int(medicamento.cantidad.to_decimal()) if isinstance(medicamento.cantidad, Decimal128) else medicamento.cantidad,
            medicamento.descripcion
        ])

    # Preparar la respuesta
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=InventarioVeterinaria.xlsx'
    wb.save(response)
    return response

def convertir_valor_decimal(valor):
    if isinstance(valor, Decimal128):
        return float(valor.to_decimal())
    return valor

def vista_previa_inventario(request):
    accesorios = Accesorios.objects.all()
    medicamentos = Medicamentos.objects.all()

    inventario = []

    for a in accesorios:
        inventario.append({
            "tipo": "Accesorio",
            "nombre": a.nombre,
            "precio": convertir_valor_decimal(a.precio),
            "cantidad": convertir_valor_decimal(a.cantidad),
            "descripcion": a.descripcion,
        })

    for m in medicamentos:
        inventario.append({
            "tipo": "Medicamento",
            "nombre": m.nombre,
            "precio": convertir_valor_decimal(m.precio),
            "cantidad": convertir_valor_decimal(m.cantidad),
            "descripcion": m.descripcion,
        })

    return render(request, 'veterinary_inventory/vista_previa_inventario.html', {
        'inventario': inventario
    })















































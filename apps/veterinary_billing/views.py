from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura, Producto, ProductoEmbebido
from .forms import ProductoForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from bson import ObjectId

def menu_principal(request):
    return render(request, 'veterinary_billing/menu.html')

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_principal')
    else:
        form = ProductoForm()
    return render(request, 'veterinary_billing/crear_producto.html', {'form': form})

def crear_factura(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        identificacion = request.POST.get('identificacion')
        direccion = request.POST.get('direccion')
        tipo_mascota = request.POST.get('tipo_mascota')
        nombre_mascota = request.POST.get('nombre_mascota')
        fecha = request.POST.get('fecha')
        precio_total = request.POST.get('precio_total')

        productos_ids = request.POST.getlist('productos')
        productos_embebidos = []

        for prod_id in productos_ids:
            if prod_id:
                try:
                    prod = Producto.objects.get(id=ObjectId(prod_id))
                    productos_embebidos.append(ProductoEmbebido(
                        nombre=prod.nombre,
                        detalle=prod.detalle,
                        precio_unitario=prod.precio_unitario
                    ))
                except Exception as e:
                    print(f"Error con producto {prod_id}: {e}")

        factura = Factura(
            nombre_cliente=nombre_cliente,
            identificacion=identificacion,
            direccion=direccion,
            tipo_mascota=tipo_mascota,
            nombre_mascota=nombre_mascota,
            fecha=fecha,
            productos=productos_embebidos,
            precio_total=precio_total
        )
        factura.save()
        return redirect('menu_principal')

    return render(request, 'veterinary_billing/crear_factura.html', {'productos': productos})

def historial_facturas(request):
    query = request.GET.get('q')
    facturas = Factura.objects.filter(identificacion=query) if query else Factura.objects.all()
    return render(request, 'veterinary_billing/historial_facturas.html', {'facturas': facturas})

def editar_factura(request, identificacion):
    factura = get_object_or_404(Factura, identificacion=identificacion)
    productos = Producto.objects.all()

    if request.method == 'POST':
        factura.nombre_cliente = request.POST.get('nombre_cliente')
        factura.identificacion = request.POST.get('identificacion')
        factura.direccion = request.POST.get('direccion')
        factura.tipo_mascota = request.POST.get('tipo_mascota')
        factura.nombre_mascota = request.POST.get('nombre_mascota')
        factura.fecha = request.POST.get('fecha')
        factura.precio_total = request.POST.get('precio_total')

        productos_ids = request.POST.getlist('productos')
        productos_embebidos = []

        for prod_id in productos_ids:
            if prod_id:
                try:
                    prod = Producto.objects.get(id=ObjectId(prod_id))
                    productos_embebidos.append(ProductoEmbebido(
                        nombre=prod.nombre,
                        detalle=prod.detalle,
                        precio_unitario=prod.precio_unitario
                    ))
                except Exception as e:
                    print(f"Error con producto {prod_id}: {e}")

        factura.productos = productos_embebidos
        factura.save()
        return redirect('historial_facturas')

    return render(request, 'veterinary_billing/editar_factura.html', {
        'factura': factura,
        'productos': productos
    })

def eliminar_factura(request, identificacion):
    factura = get_object_or_404(Factura, identificacion=identificacion)
    factura.delete()
    return redirect('historial_facturas')

def exportar_pdf(request, identificacion):
    factura = get_object_or_404(Factura, identificacion=identificacion)
    template_path = 'veterinary_billing/factura_pdf.html'
    context = {'factura': factura}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{identificacion}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error al generar PDF', status=500)

    return response

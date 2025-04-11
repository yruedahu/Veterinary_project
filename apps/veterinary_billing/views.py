from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura
from .forms import FacturaForm
from django.http import HttpResponse

def billing_home(request):
    return HttpResponse("¡Veterinary Billing está funcionando!")

def listar_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'veterinary_billing/facturas.html', {'facturas': facturas})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm()
    return render(request, 'veterinary_billing/form_factura.html', {'form': form})

def editar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'veterinary_billing/form_factura.html', {'form': form})

def eliminar_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    factura.delete()
    return redirect('listar_facturas')


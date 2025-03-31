from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HistoriaClinicaForm
from .models import HistoriaClinica

def nueva_historia_clinica(request):
    form = HistoriaClinicaForm()
    
    if request.method == "POST":
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Historia clínica guardada con éxito.")

    return render(request, 'veterinary_clinic/historia_clinica.html', {'form': form})

def listar_historias(request):
    historias = HistoriaClinica.objects.all()
    return render(request, 'veterinary_clinic/listado_historias.html', {'historias': historias})

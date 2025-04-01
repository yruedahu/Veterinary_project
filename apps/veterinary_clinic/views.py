from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HistoriaClinicaForm
from .models import HistoriaClinica
from .forms.historia_clinica_form import HistoriaClinicaForm

def nueva_historia_clinica(request):
    form = HistoriaClinicaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Historia clínica guardada con éxito.")
    
    return render(request, "veterinary_clinic/historia_clinica.html", {"form": form})

def listar_historias(request):
    historias = HistoriaClinica.objects.all()
    return render(request, 'veterinary_clinic/listado_historias.html', {'historias': historias})

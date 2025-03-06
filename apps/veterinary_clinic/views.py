from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import HistoriaClinicaForm

def clinic_home(request):
    return HttpResponse("¡Veterinary Clinic está funcionando!")

def nueva_historia_clinica(request):
    form = HistoriaClinicaForm()  # Instancia del formulario
    return render(request, 'veterinary_clinic/historia_clinica.html', {'form': form})


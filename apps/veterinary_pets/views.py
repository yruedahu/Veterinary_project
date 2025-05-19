from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet

def pets_home(request):
    return render(request, 'mascotas.html')

def mascotas_list(request):
    mascotas = Pet.objects.all()
    return render(request, 'mascotas_list.html', {'mascotas': mascotas})

def mascotas_toy(request):
    return render(request, 'mascotas_toy.html')

def mascotas_visit(request):
    return render(request, 'mascotas_visit.html')
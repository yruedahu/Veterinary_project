from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import HistoriaClinicaForm
from .models import HistoriaClinica
from .models.especie import Especie
from .models.raza import Raza
from .models.departamento import Departamento
from .models.ciudad import Ciudad
from .forms.historia_clinica_form import HistoriaClinicaForm
from bson import ObjectId
from django.utils import timezone
import datetime


def nueva_historia_clinica(request):
    if request.method == "POST":
        form = HistoriaClinicaForm(request.POST)

        # Cargar manualmente los FKs
        form.fields['especie'].queryset = Especie.objects.all()
        form.fields['raza'].queryset = Raza.objects.all()
        form.fields['departamento'].queryset = Departamento.objects.all()
        form.fields['ciudad'].queryset = Ciudad.objects.all()

        # Parsear fecha
        fecha_raw = request.POST.get("fecha_atencion")
        try:
            fecha_atencion = timezone.make_aware(datetime.datetime.strptime(fecha_raw, "%Y-%m-%d"))
        except Exception as e:
            print("Error parseando fecha:", e)
            fecha_atencion = timezone.now()

        if form.is_valid():
            form.save()
            messages.success(request, "Historia clínica guardada con éxito.")
            return redirect("nueva_historia_clinica")
        else:
            print("Errores del formulario:", form.errors)

            historia = HistoriaClinica(
                nombre_mascota=request.POST.get("nombre_mascota"),
                edad=request.POST.get("edad"),
                duenio=request.POST.get("duenio"),
                telefono_contacto=request.POST.get("telefono_contacto"),
                motivo_consulta=request.POST.get("motivo_consulta"),
                fecha_atencion=fecha_atencion,
            )
            try:
                historia.especie = Especie.objects.get(_id=ObjectId(request.POST.get("especie")))
                historia.raza = Raza.objects.get(_id=ObjectId(request.POST.get("raza")))
                historia.departamento = Departamento.objects.get(_id=ObjectId(request.POST.get("departamento")))
                historia.ciudad = Ciudad.objects.get(_id=ObjectId(request.POST.get("ciudad")))
            except Exception as e:
                print("Error asignando FK:", e)

            historia.save()
            messages.success(request, "Historia clínica guardada manualmente.")
            return redirect("nueva_historia_clinica")
    else:
        form = HistoriaClinicaForm()
        form.fields['especie'].queryset = Especie.objects.all()
        form.fields['raza'].queryset = Raza.objects.all()
        form.fields['departamento'].queryset = Departamento.objects.all()
        form.fields['ciudad'].queryset = Ciudad.objects.all()

    return render(request, "veterinary_clinic/historia_clinica.html", {"form": form})


def listar_historias(request):
    historias = HistoriaClinica.objects.all()
    return render(request, 'veterinary_clinic/listado_historias.html', {'historias': historias})


def cargar_razas(request):
    especie_id = request.GET.get('especie_id')
    try:
        especie_oid = ObjectId(especie_id)
    except Exception as e:
        print("ID inválido:", especie_id)
        return JsonResponse([], safe=False)

    razas_queryset = Raza.objects.filter(especie_id=especie_oid).values('_id', 'nombre')
    
    # Convertir ObjectId a string manualmente
    razas = [{'_id': str(raza['_id']), 'nombre': raza['nombre']} for raza in razas_queryset]
    
    print("Razas encontradas:", razas)
    return JsonResponse(razas, safe=False)

def cargar_ciudades(request):
    departamento_id = request.GET.get('departamento_id')
    try:
        departamento_oid = ObjectId(departamento_id)
    except Exception as e:
        print('ID no válido', departamento_id)
        return JsonResponse([], safe=False)
    
    
    ciudades_queryset = Ciudad.objects.filter(departamento_id=departamento_oid).values('_id', 'nombre')
    
    ciudades = [{'_id': str(ciudad['_id']), 'nombre':ciudad['nombre']} for ciudad in ciudades_queryset]
    print("Ciudades encontradas:", ciudades)
    return JsonResponse(ciudades, safe=False)


def ver_historia(request, id):
    historia = HistoriaClinica.objects.get(_id=ObjectId(id))
    historia.id = str(historia._id)  # 👈 le damos un alias accesible
    return render(request, 'veterinary_clinic/detalle_historia.html', {'historia': historia})

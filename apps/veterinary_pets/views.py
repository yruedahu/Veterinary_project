from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pet, Owner, Toy, Especie, Visit
from datetime import datetime
from openpyxl import Workbook

def mascotas_list(request):
    mascotas = Pet.objects.all()
    return render(request, 'mascotas_home.html', {'mascotas': mascotas})


def mascotas_toy(request):
    mascotas = Pet.objects.all()

    if request.method == 'POST':
        nombre_juguete = request.POST.get('name')
        descripcion = request.POST.get('description')
        mascotas_ids = request.POST.getlist('pet')

        if nombre_juguete:
            toy = Toy.objects.create(name=nombre_juguete, description=descripcion)
            toy.pet.set(mascotas_ids)
            toy.save()

            return redirect('mascotas_list')
        else:
            return render(request, 'mascotas_toy.html', {
                'mascotas': mascotas,
                'error': 'Debes ingresar un nombre para el juguete.'
            })

    return render(request, 'mascotas_toy.html', {'mascotas': mascotas})

def pets_home(request, mascota_id=None):
    mascota = None
    if mascota_id:
        mascota = get_object_or_404(Pet, id=mascota_id)

    propietarios = Owner.objects.all()
    especies = Especie.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('mascota')
        edad = request.POST.get('edad')
        especie_id = request.POST.get('especie')
        nueva_especie = request.POST.get('nueva_especie')
        propietario_id = request.POST.get('propietario')
        foto_url = request.POST.get('foto_url')

        if nueva_especie:
            especie, _ = Especie.objects.get_or_create(specie=nueva_especie)
        else:
            especie = Especie.objects.get(id=especie_id)

        propietario = Owner.objects.get(id=propietario_id)

        if mascota:
            mascota.name = nombre
            mascota.age = edad
            mascota.specie = especie
            mascota.owner = propietario
            mascota.picture = foto_url
            mascota.save()
        else:
            mascota = Pet.objects.create(
                name=nombre,
                age=edad,
                specie=especie,
                owner=propietario,
                picture=foto_url
            )
        
        return redirect('mascotas_list')

    return render(request, 'mascotas_form.html', {
        'mascota': mascota,
        'propietarios': propietarios,
        'especies': especies
    })

def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Pet, id=mascota_id)
    mascota.delete()
    return redirect('mascotas_list')

def mascotas_resumen(request):
    mascotas = Pet.objects.all()
    resumen = []

    nombres_mascotas = []
    cantidad_visitas = []

    for mascota in mascotas:
        ultima_visita = mascota.visit_set.order_by('-date').first()
        juguetes = mascota.toy_set.all()

        resumen.append({
            'propietario': mascota.owner.name,
            'mascota': mascota.name,
            'edad': mascota.age,
            'juguete': ', '.join([j.name if j.name else 'Sin nombre' for j in juguetes]) if juguetes else 'Ninguno',
            'ultima_visita': ultima_visita.date.strftime('%Y-%m-%d %H:%M') if ultima_visita else 'Sin visitas'
        })

        nombres_mascotas.append(mascota.name)
        cantidad_visitas.append(mascota.visit_set.count())

    contexto = {
        'resumen': resumen,
        'nombres_mascotas': nombres_mascotas,
        'cantidad_visitas': cantidad_visitas,
    }

    return render(request, 'mascotas_resumen.html', contexto)

def exportar_resumen_excel(request):
    mascotas = Pet.objects.all()
    wb = Workbook()
    ws = wb.active
    ws.title = "Resumen Mascotas"

    # Encabezados
    ws.append(["Propietario", "Nombre de Mascota", "Edad", "Juguete Asignado", "Última Visita"])

    for mascota in mascotas:
        ultima_visita = mascota.visit_set.order_by('-date').first()
        juguete = mascota.toy_set.first()

        ws.append([
            mascota.owner.name,
            mascota.name,
            mascota.age,
            juguete.name if juguete else 'Ninguno',
            ultima_visita.date.strftime('%Y-%m-%d') if ultima_visita else 'Sin visitas'
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=ResumenMascotas.xlsx'
    wb.save(response)
    return response

def mascotas_visit(request):
    mascotas = Pet.objects.all()

    if request.method == 'POST':
        pet_id = request.POST.get('pet')
        fecha_str = request.POST.get('date')
        razon_seleccionada = request.POST.get('reason_select')
        razon_otro = request.POST.get('reason_text')

        pet = get_object_or_404(Pet, id=pet_id)
        fecha = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M")

        razon = razon_otro if razon_seleccionada == "Otro" else razon_seleccionada

        Visit.objects.create(
            pet=pet,
            date=fecha,
            reason=razon
        )
        return redirect('mascotas_list')

    return render(request, 'mascotas_visit.html', {'mascotas': mascotas})
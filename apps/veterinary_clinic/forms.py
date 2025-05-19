from django import forms
from .models.historia_clinica import HistoriaClinica
from .models.especie import Especie
from .models.raza import Raza
from .models.departamento import Departamento
from .models.ciudad import Ciudad

class HistoriaClinicaForm(forms.ModelForm):
    especie = forms.ModelChoiceField(
        queryset=Especie.objects.all(),
        to_field_name='_id',
        empty_label="Seleccione una especie"
    )

    raza = forms.ModelChoiceField(
        queryset=Raza.objects.all(),
        to_field_name='_id',
        empty_label="Seleccione una raza"
    )

    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all(),
        to_field_name='_id',
        empty_label="Seleccione un departamento"
    )

    ciudad = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        to_field_name='_id',
        empty_label="Seleccione una ciudad"
    )

    class Meta:
        model = HistoriaClinica
        fields = '__all__'

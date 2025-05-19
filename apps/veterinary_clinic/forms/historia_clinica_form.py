from django import forms
from bson import ObjectId
from ..models.historia_clinica import HistoriaClinica
from ..models.especie import Especie
from ..models.raza import Raza
from ..models.departamento import Departamento
from ..models.ciudad import Ciudad

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            "nombre_mascota",
            "especie",
            "raza",
            "edad",
            "duenio",
            "telefono_contacto",
            "motivo_consulta",
            "departamento",
            "ciudad",
            "fecha_atencion",
        ]
        widgets = {
            "fecha_atencion": forms.DateInput(attrs={"type": "date"}),
            "motivo_consulta": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super(HistoriaClinicaForm, self).__init__(*args, **kwargs)
        self.fields["especie"].queryset = Especie.objects.all()
        self.fields["raza"].queryset = Raza.objects.none()
        self.fields["departamento"].queryset = Departamento.objects.all()
        self.fields["ciudad"].queryset = Ciudad.objects.none()

        if "especie" in self.data:
            try:
                especie_id = ObjectId(self.data.get("especie"))
                self.fields["raza"].queryset = Raza.objects.filter(especie_id=especie_id)
            except (ValueError, TypeError):
                pass  

        if "departamento" in self.data:
            try:
                departamento_id = ObjectId(self.data.get("departamento"))
                self.fields["ciudad"].queryset = Ciudad.objects.filter(departamento_id=departamento_id)
            except (ValueError, TypeError):
                pass  

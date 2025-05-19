from django import forms
from .models import Accesorios,Medicamentos,Proveedores

class AccesoriosForm(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ["nombre", "precio", "cantidad","descripcion","imagen"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del accesorio"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Precio"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Cantidad"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción", "rows": 3}),
            "imagen": forms.URLInput(attrs={"class": "form-control", "placeholder": "URL de la imagen"}),
        }


class MedicamentosForm(forms.ModelForm):
    class Meta: 
        model = Medicamentos
        fields =["nombre", "precio", "cantidad", "descripcion","imagen"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del medicamento"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Precio"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Cantidad"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción", "rows": 3}),
            "imagen": forms.URLInput(attrs={"class": "form-control", "placeholder": "URL de la imagen"}),
        }

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ["nombre", "servicio_producto", "contacto", "ubicacion","estado"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del proveedor"}),
            "servicio_producto": forms.Select(choices=Proveedores.TIPO_SERVICIO_CHOICES),
            "contacto": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Contacto"}),
            "ubicacion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ubicación"}),
            "estado": forms.Select(choices=Proveedores.TIPO_ESTADO),
        }

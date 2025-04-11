from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "cantidad", "precio", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del producto"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Cantidad"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Precio"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descripción", "rows": 3}),
        }
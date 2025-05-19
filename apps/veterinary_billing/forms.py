from django import forms
from .models import Producto, Factura

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

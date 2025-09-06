from django.urls import path
from .views import inventory_home, agregar_producto, eliminar_producto, editar_producto

urlpatterns = [
    path('', inventory_home, name='inventory_home'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
]

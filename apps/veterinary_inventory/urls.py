from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inventory_home, name='inventory_home'),

    path('exportar-inventario/', views.exportar_inventario, name='exportar_inventario'),
    path('vista-previa-inventario/', views.vista_previa_inventario, name='vista_previa_inventario'),


    #ACCESORIOS
    path('agregar_accesorios/', views.agregar_accesorios, name='agregar_accesorios'),
    path('editar/<str:accesorios_id>/', views.editar_accesorios, name='editar_accesorios'),
    path('eliminar/<str:accesorios_id>/', views.eliminar_accesorios, name='eliminar_accesorios'),
    path('detalle_accesorios/', views.detalle_accesorios, name='detalle_accesorios'),


    #PROVEEDORES
    path('agregar_proveedores/', views.agregar_proveedores, name='agregar_proveedores'),
    path('editar_proveedores/<str:proveedor_id>/', views.editar_proveedores, name='editar_proveedores'),
    path('eliminar_proveedores/<str:proveedor_id>/', views.eliminar_proveedores, name='eliminar_proveedores'),
    path('detalle_proveedores/', views.detalle_proveedores, name='detalle_proveedores'),


    #MEDICAMENTOS
    path('agregar_medicamentos/', views.agregar_medicamentos, name='agregar_medicamentos'),
    path('editar_medicamentos/<str:medicamentos_id>/', views.editar_medicamentos, name='editar_medicamentos'),
    path('eliminar_medicamentos/<str:medicamentos_id>/', views.eliminar_medicamentos, name='eliminar_medicamentos'),
    path('detalle_medicamentos/', views.detalle_medicamentos, name='detalle_medicamentos'),













]

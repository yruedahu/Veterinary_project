from django.urls import path
from . import views

urlpatterns = [
    path('facturacion/', views.menu_principal, name='menu_principal'),
    path('crear-factura/', views.crear_factura, name='crear_factura'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('historial-facturas/', views.historial_facturas, name='historial_facturas'),
    path('editar-factura/<str:identificacion>/', views.editar_factura, name='editar_factura'),
    path('eliminar-factura/<str:identificacion>/', views.eliminar_factura, name='eliminar_factura'),
    path('exportar-pdf/<str:identificacion>/', views.exportar_pdf, name='exportar_pdf'),
]

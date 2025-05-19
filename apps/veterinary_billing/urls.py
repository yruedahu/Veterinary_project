from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_home, name='billing_home'),
    path('', views.billing_home, name='billing_home'),
    path('facturas/', views.listar_facturas, name='listar_facturas'),
    path('facturas/nueva/', views.crear_factura, name='crear_factura'),
    path('facturas/editar/<str:pk>/', views.editar_factura, name='editar_factura'),
    path('facturas/eliminar/<str:pk>/', views.eliminar_factura, name='eliminar_factura'),

]

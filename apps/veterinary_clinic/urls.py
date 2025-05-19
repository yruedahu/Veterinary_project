from django.urls import path
from . import views  # Importamos views correctamente

urlpatterns = [
    path('historia-clinica/', views.nueva_historia_clinica, name='nueva_historia_clinica'),
    path('listado-historias/', views.listar_historias, name='listado_historias'),
    path('ajax/cargar-razas/', views.cargar_razas, name='ajax_cargar_razas'),
    path('ajax/cargar-ciudades/', views.cargar_ciudades, name='ajax_cargar_ciudades'),
    path('historia/<str:id>/', views.ver_historia, name='ver_historia'),
    ]


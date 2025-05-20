from django.urls import path, include
from . import views  # Importamos views correctamente

urlpatterns = [
    path('', views.clinic_home, name='clinic_home'),
    path('historia-clinica/', views.nueva_historia_clinica, name='nueva_historia_clinica'),
    path('listado-historias/', views.listar_historias, name='listado_historias'),
    path('ajax/cargar-razas/', views.cargar_razas, name='ajax_cargar_razas'),
    path('ajax/cargar-ciudades/', views.cargar_ciudades, name='ajax_cargar_ciudades'),
    path('historia/<str:id>/', views.ver_historia, name='ver_historia'),
    path('historia/eliminar/<str:id>/', views.eliminar_historia_clinica, name='eliminar_historia_clinica'),
    path('historia/<str:historia_id>/diagnostico/', views.guardar_diagnostico, name='guardar_diagnostico'),
    path('historia/<str:historia_id>/exportar/', views.exportar_historia_pdf, name='exportar_historia_pdf'),
    #path('historia/<str:historia_id>/detalle/', views.ver_historia, name='ver_historia'),
    ]


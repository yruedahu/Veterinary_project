from django.urls import path
from . import views  # Importamos views correctamente

urlpatterns = [
    path('historia-clinica/', views.nueva_historia_clinica, name='nueva_historia_clinica'),
    path('listado-historias/', views.listar_historias, name='listado_historias'),
]

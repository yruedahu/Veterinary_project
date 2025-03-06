from django.urls import path
from . import views  # Importamos views correctamente

urlpatterns = [
    path('', views.clinic_home, name='clinic_home'),
    path('historia-clinica/', views.nueva_historia_clinica, name='nueva_historia_clinica'),
]

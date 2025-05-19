from django.urls import path
from .views import pets_home, mascotas_list,mascotas_toy, mascotas_visit

urlpatterns = [
    path('mascotas/', pets_home, name='pets_home'),
    path('mascotas/listado/', mascotas_list, name='mascotas_list'),
    path('mascotas/toy/', mascotas_toy, name='mascotas_toy'),
    path('mascotas/visit/', mascotas_visit, name='mascotas_visit'),
]
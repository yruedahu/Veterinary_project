from django.urls import path
from .views import pets_home

urlpatterns = [
    path('mascotas/', pets_home, name='pets_home'),
]

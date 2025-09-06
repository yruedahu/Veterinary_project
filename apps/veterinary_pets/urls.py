from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('mascotas/', views.pets_home, name='pets_home'),
    path('mascotas/listado/', views.mascotas_list, name='mascotas_list'),
    path('mascotas/toy/', views.mascotas_toy, name='mascotas_toy'),
    path('mascotas/visit/', views.mascotas_visit, name='mascotas_visit'),
    path('mascota/nueva/', views.pets_home, name='crear_mascota'),
    path('mascotas/<int:mascota_id>/editar/', views.pets_home, name='editar_mascota'),
    path('mascotas/eliminar/<int:mascota_id>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('mascotas/resumen/', views.mascotas_resumen, name='mascotas_resumen'),
    path('pets/exportar_excel/', views.exportar_resumen_excel, name='exportar_resumen_excel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
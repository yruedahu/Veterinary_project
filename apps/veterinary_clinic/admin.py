from django.contrib import admin
from .models.historia_clinica import HistoriaClinica
from .models.especie import Especie
from .models.raza import Raza
from .models.departamento import Departamento
from .models.ciudad import Ciudad

# Registrar modelos en el panel de administración
admin.site.register(HistoriaClinica)
admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(Departamento)
admin.site.register(Ciudad)

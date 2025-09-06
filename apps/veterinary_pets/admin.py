from django.contrib import admin
from .models import Pet, Especie, Owner, Visit, Toy

admin.site.register(Pet)
admin.site.register(Especie)
admin.site.register(Owner)
admin.site.register(Visit)
admin.site.register(Toy)
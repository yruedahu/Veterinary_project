from django.contrib import admin
from .models import User, Veterinarian, Receptionist, Client

admin.site.register(User)
admin.site.register(Veterinarian)
admin.site.register(Receptionist)
admin.site.register(Client)


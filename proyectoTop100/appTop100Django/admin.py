from django.contrib import admin
from django.contrib import admin
from .models import Cancion, Interprete, Estilo,Voto
admin.site.register(Cancion)
admin.site.register(Interprete)
admin.site.register(Estilo)
admin.site.register(Voto)


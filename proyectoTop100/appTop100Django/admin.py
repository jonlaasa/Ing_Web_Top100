from django.contrib import admin
from .models import Cancion, Interprete, Estilo, Voto
from django.utils.html import format_html

# Personalización avanzada para el modelo Estilo
class EstiloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'total_canciones')
    search_fields = ['nombre', 'descripcion']
    list_filter = ['nombre']
    ordering = ['nombre']
    
    # Método adicional para mostrar el total de canciones asociadas a un estilo
    def total_canciones(self, obj):
        return obj.cancion_set.count()
    total_canciones.short_description = 'Número de Canciones'

admin.site.register(Estilo, EstiloAdmin)

# Personalización avanzada para el modelo Interprete
class InterpreteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_integrantes', 'oyentes_mensuales', 'imagen_thumbnail')
    search_fields = ['nombre', 'descripcion_interprete']
    list_filter = ['numero_integrantes']
    list_editable = ('numero_integrantes',)
    ordering = ['nombre']
    actions = ['increase_oyentes_mensuales']
    
    # Mostrar imagen en miniatura en la vista de lista
    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" alt="Imagen Interprete" width="50" height="50">', obj.imagen.url)
        return 'Sin Imagen'
    imagen_thumbnail.short_description = 'Imagen'
    
    # Acción personalizada para incrementar oyentes mensuales
    def increase_oyentes_mensuales(self, request, queryset):
        for interprete in queryset:
            interprete.oyentes_mensuales += 100000  # Aumentar 100000 oyentes
            interprete.save()
        self.message_user(request, "¡Oyentes mensuales incrementados!")
    increase_oyentes_mensuales.short_description = 'Incrementar oyentes mensuales'

admin.site.register(Interprete, InterpreteAdmin)

# Inline para el modelo Voto
class VotoInline(admin.TabularInline):
    model = Voto
    extra = 1  # Número de filas vacías para agregar nuevos votos
    fields = ('valor', 'fecha',)
    readonly_fields = ('fecha',)  # Hacer la fecha solo lectura
    can_delete = True  # Permitir eliminación directa

# Personalización avanzada para el modelo Cancion
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estilo', 'ranking', 'fecha', 'imagen_thumbnail')
    search_fields = ['titulo', 'estilo__nombre']
    list_filter = ['fecha', 'estilo']
    filter_horizontal = ('intepretes',)
    autocomplete_fields = ['estilo']  # Mejor experiencia al buscar estilos
    actions = ['reset_ranking']
    inlines = [VotoInline]  # Añadir Votos como inline
    
    # Mostrar imagen en miniatura en la vista de lista
    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" alt="Imagen Cancion" width="50" height="50">', obj.imagen.url)
        return 'Sin Imagen'
    imagen_thumbnail.short_description = 'Imagen'
    
    # Acción personalizada para resetear el ranking
    def reset_ranking(self, request, queryset):
        for cancion in queryset:
            cancion.ranking = 0
            cancion.save()
        self.message_user(request, "Ranking de las canciones reseteado")
    reset_ranking.short_description = 'Resetear ranking de canciones'

admin.site.register(Cancion, CancionAdmin)

# Personalización avanzada para el modelo Voto
class VotoAdmin(admin.ModelAdmin):
    list_display = ('cancion', 'valor', 'fecha')
    list_filter = ['fecha']
    search_fields = ['cancion__titulo']
    actions = ['change_voto_to_5']
    
    # Acción personalizada para cambiar el valor de los votos a 5
    def change_voto_to_5(self, request, queryset):
        queryset.update(valor=5)
        self.message_user(request, "Todos los votos han sido cambiados a 5")
    change_voto_to_5.short_description = 'Cambiar valor de voto a 5'

admin.site.register(Voto, VotoAdmin)


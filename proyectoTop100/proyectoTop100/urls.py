from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns  # Importa i18n_patterns

# Configuración de URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # Ruta para manejar los idiomas
]

# Aplica i18n_patterns para las rutas que se deben adaptar al idioma
urlpatterns += i18n_patterns(
    path('appTop100Django/', include('appTop100Django.urls')),  # Esto será accesible con el idioma
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

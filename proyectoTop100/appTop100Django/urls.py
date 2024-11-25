# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Página principal -- La mejor por género
    path('', views.index, name='index'),

    # Otras rutas...
    path('canciones/', views.lista_canciones, name='lista_canciones'),
    path('canciones/<int:cancion_id>/', views.detalles_cancion, name='detalles_cancion'),
    path('estilos/', views.lista_estilos, name='lista_estilos'),
    path('estilos/<int:estilo_id>/', views.detalles_estilo, name='detalles_estilo'),
    path('interpretes/', views.lista_interpretes, name='lista_interpretes'),
    path('interpretes/<int:interprete_id>/', views.detalles_interprete, name='detalles_interprete'),
    path('cancionAjax/<int:cancion_id>/', views.ajax, name='ajax'),
]

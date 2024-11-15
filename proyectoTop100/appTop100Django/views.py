from .models import Estilo, Interprete, Cancion
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from .models import Estilo, Interprete, Cancion

def index(request):
    estilos = Estilo.objects.all()  # Obtiene todos los estilos
    top_canciones_por_estilo = []  
    for estilo in estilos:
        cancion = Cancion.objects.filter(estilo=estilo).order_by('ranking').first()  # La mejor canción del estilo
        if cancion:
            top_canciones_por_estilo.append((estilo, cancion))  # Guarda una tupla (estilo, cancion)
    
    context = {
        'top_canciones_por_estilo': top_canciones_por_estilo,  # Cambiado el contexto
    }
    return render(request, 'index.html', context)


########### CANCIONES ################3
# Visualizar la lista de canciones
def lista_canciones(request):
    canciones = Cancion.objects.order_by('ranking').all()
    context = {'canciones': canciones}
    return render(request, 'lista_canciones.html', context)

# Detalles de una canción
def detalles_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, pk=cancion_id)
    interpretes = cancion.intepretes.all()
    estilo = cancion.estilo  # Accediendo al estilo de la canción
    context = {
        'cancion': cancion,
        'interpretes': interpretes,
        'estilo': estilo  # Agregando el estilo al contexto
    }
    return render(request, 'detalles_cancion.html', context)
#########################################################


########### ESTILOS #########################################
# Visualizar la lista de estilos musicales
def lista_estilos(request):
    estilos = Estilo.objects.all()
    context = {'estilos': estilos}
    return render(request, 'lista_estilos.html', context)

# Detalles de un estilo específico y sus canciones
def detalles_estilo(request, estilo_id):
    estilo = get_object_or_404(Estilo, pk=estilo_id)
    canciones = estilo.cancion_set.all().order_by('ranking')
    context = {'estilo': estilo, 'canciones': canciones}
    return render(request, 'detalles_estilo.html', context)
############################################################


############### INTERPRETES #############################3
def lista_interpretes(request):
    interpretes = Interprete.objects.order_by('nombre').all()
    context = {'interpretes': interpretes}
    return render(request, 'lista_interpretes.html', context)

def detalles_interprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, pk=interprete_id)
    canciones = interprete.cancion_set.all().order_by('titulo')
    context = {'interprete': interprete, 'canciones': canciones}
    return render(request, 'detalles_interprete.html', context)

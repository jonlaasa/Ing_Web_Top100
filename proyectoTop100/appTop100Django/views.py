from .models import Estilo, Interprete, Cancion,Voto
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render,redirect
from django.contrib import messages
from django.utils.timezone import now
from django_ratelimit.decorators import ratelimit

# Página principal
def index(request):
    estilos = get_list_or_404(Estilo.objects.all()) # Obtiene todos los estilos
    top_canciones_por_estilo = []  
    for estilo in estilos:
        # Obtiene la mejor canción del estilo según el ranking
        cancion = Cancion.objects.filter(estilo=estilo).order_by('ranking').first()
        if cancion:
            top_canciones_por_estilo.append((estilo, cancion))
    
    context = {
        'top_canciones_por_estilo': top_canciones_por_estilo,  # Envía (estilo, canción) al contexto
    }
    return render(request, 'index.html', context)


########### CANCIONES ################
# Visualizar la lista de canciones
def lista_canciones(request):
    canciones = get_list_or_404(Cancion.objects.order_by('ranking').all())
    context = {'canciones': canciones}
    return render(request, 'lista_canciones.html', context)

def formulario(request):
    canciones = get_list_or_404(Cancion.objects.all())
    context = {'canciones': canciones}
    return render(request, 'formulario.html', context)

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


########### ESTILOS ######################################
# Visualizar la lista de estilos musicales
def lista_estilos(request):
    estilos = get_list_or_404(Estilo.objects.all())
    context = {'estilos': estilos}
    return render(request, 'lista_estilos.html', context)

# Detalles de un estilo específico y sus canciones
def detalles_estilo(request, estilo_id):
    estilo = get_object_or_404(Estilo, pk=estilo_id)
    canciones = estilo.cancion_set.all().order_by('ranking')
    context = {'estilo': estilo, 'canciones': canciones}
    return render(request, 'detalles_estilo.html', context)
############################################################


############### INTERPRETES ##############################
def lista_interpretes(request):
    interpretes = get_list_or_404(Interprete.objects.order_by('nombre').all())
    context = {'interpretes': interpretes}
    return render(request, 'lista_interpretes.html', context)

def detalles_interprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, pk=interprete_id)
    canciones = interprete.cancion_set.all().order_by('titulo')
    context = {'interprete': interprete, 'canciones': canciones}
    return render(request, 'detalles_interprete.html', context)

################ AJAX #####################################
# Devuelve la imagen de una canción
def ajax(request, cancion_id):
    cancion = get_object_or_404(Cancion, pk=cancion_id)
    context = { 'cancion': cancion }
    return render(request, 'ajax.html', context)

####### REGISTRAR VOTOS FORMULARIO ################
@ratelimit(key='ip', rate='5/m', method='ALL')
def registrar_votos(request):
    if request.method == 'POST':
        # Obtener la lista de canciones seleccionadas
        canciones_seleccionadas = request.POST.getlist('canciones')

        for cancion_id in canciones_seleccionadas:
            try:

                # Buscar la canción por ID
                if not cancion_id.isdigit():  # Evitar inyecciones
                    continue # Se ignora si no en numerico

                cancion = get_object_or_404(Cancion, id=cancion_id)

                # Crear un nuevo registro de voto para esta canción
                Voto.objects.create(cancion=cancion, valor=1, fecha=now())
    
            except Cancion.DoesNotExist:
                continue  # Si no existe la canción, la ignoramos

        # Redirigir al index con un mensaje de éxito
        messages.success(request, "Voto registrado correctamente")
        return redirect('index')  # Cambiar a la vista que maneja tu index
    else:
        # Si no es un GET, redirigir al formulario
        return redirect('formulario')  # O a la URL que corresponda para el formulario

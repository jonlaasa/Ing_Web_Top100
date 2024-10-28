from django.db import models

class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nombre  
       
class Interprete(models.Model):
    nombre = models.CharField(max_length=50)
    numero_integrantes = models.IntegerField(default=0)
    descripcion_interprete = models.CharField(max_length=300)
    oyentes_mensuales = models.IntegerField(default=0)  
    imagen = models.ImageField(upload_to='interpretes/', blank=True, null=True)  
    
    def __str__(self):
        return self.nombre  
    
class Cancion(models.Model):
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField(default=0)
    ranking = models.IntegerField(unique=True)
    fecha = models.DateField()
    # FOREIGN
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    intepretes = models.ManyToManyField(Interprete) 
    
    def __str__(self):
        return self.titulo 

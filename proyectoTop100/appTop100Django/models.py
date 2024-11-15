from django.db import models


#Clase estilo con su nombre y descripcion
class Estilo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nombre  
       


#Clase interprete con su nombre.. integrantes, oyentes mensuales E IMAGEN
class Interprete(models.Model):
    nombre = models.CharField(max_length=50)
    numero_integrantes = models.IntegerField(default=0)
    descripcion_interprete = models.CharField(max_length=300)
    oyentes_mensuales = models.IntegerField(default=0)  
    imagen = models.ImageField(upload_to='interpretes/', blank=True, null=True)  
    
    def __str__(self):
        return self.nombre  
    
    
    # Clase cancion con ranking IMAGEN... y dos foreign key asociadas al estilo e interprete de dicha csncion
class Cancion(models.Model):
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField(default=0)
    ranking = models.IntegerField(unique=True)
    fecha = models.DateField()
    # FOREIGN
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    intepretes = models.ManyToManyField(Interprete) 
    imagen = models.ImageField(upload_to='canciones/', blank=True, null=True)  
    def __str__(self):
        return self.titulo 

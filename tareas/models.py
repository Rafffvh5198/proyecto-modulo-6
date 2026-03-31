from django.db import models
from django.contrib.auth.models import User  #queda registrado el usuario que creo el proyecto

# Create your models here.
class Proyecto(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    usuario=models.ForeignKey(User,on_delete=models.CASCADE) #se borra el usuario se borra todo lo relativo a el
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo=models.CharField(max_length=200)
    descripcion=models.TextField()
    completada=models.BooleanField(default=False)
    proyecto= models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
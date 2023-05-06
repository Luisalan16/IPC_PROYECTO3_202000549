from django.db import models
from django.utils import timezone

# Create your models here.
class File(models.Model):
    archivo = models.FileField()
    

    def __str__(self):
        return "Autor: " + str(self.autor) + "\nContenido: " + str(self.Contenido)
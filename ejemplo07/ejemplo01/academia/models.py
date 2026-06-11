from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()


    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.cedula} - edad: {self.edad}"
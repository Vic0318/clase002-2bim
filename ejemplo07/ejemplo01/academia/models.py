from django.db import models
from datetime import datetime


# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()


    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.cedula} - Ciudad/Provincia: {self.obtener_ciudad()} - Edad: {self.edad} - Año de nacimiento: {self.obtener_anio()}"

    def obtener_anio(self):
        anio_actual = datetime.now().year
        valor = anio_actual - self.edad
        return valor

    def obtener_ciudad(self):
        if not self.cedula or len(self.cedula) < 2:
            return "Desconocida"
        
        codigo = self.cedula[:2]
        provincias = {
            "01": "Azuay (Cuenca)",
            "02": "Bolívar (Guaranda)",
            "03": "Cañar (Azogues)",
            "04": "Carchi (Tulcán)",
            "05": "Cotopaxi (Latacunga)",
            "06": "Chimborazo (Riobamba)",
            "07": "El Oro (Machala)",
            "08": "Esmeraldas (Esmeraldas)",
            "09": "Guayas (Guayaquil)",
            "10": "Imbabura (Ibarra)",
            "11": "Loja (Loja)",
            "12": "Los Ríos (Babahoyo)",
            "13": "Manabí (Portoviejo)",
            "14": "Morona Santiago (Macas)",
            "15": "Napo (Tena)",
            "16": "Pastaza (Puyo)",
            "17": "Pichincha (Quito)",
            "18": "Tungurahua (Ambato)",
            "19": "Zamora Chinchipe (Zamora)",
            "20": "Galápagos (Puerto Baquerizo Moreno)",
            "21": "Sucumbíos (Nueva Loja)",
            "22": "Orellana (Francisco de Orellana)",
            "23": "Santo Domingo de los Tsáchilas (Santo Domingo)",
            "24": "Santa Elena (Santa Elena)",
            "30": "Exterior"
        }
        return provincias.get(codigo, "Desconocida")
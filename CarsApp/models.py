from django.db import models

class Americano(models.Model):
    marca_de_vehiculo = models.CharField(max_length = 15)
    modelo_de_vehiculo = models.CharField(max_length = 15)
    motor = models.CharField(max_length = 20)
    descripcion_vehiculo = models.CharField(max_length = 100)
    nacionalidad_de_fabricante = models.CharField(max_length = 15)

    def __str__(self):
        return f"{self.id} - {self.marca_de_vehiculo} - {self.modelo_de_vehiculo} - {self.nacionalidad_de_fabricante}"

class Europeo(models.Model):
    marca_de_vehiculo = models.CharField(max_length = 15)
    modelo_de_vehiculo = models.CharField(max_length = 15)
    motor = models.CharField(max_length = 20)
    descripcion_vehiculo = models.CharField(max_length = 100)
    nacionalidad_de_fabricante = models.CharField(max_length = 15)

    def __str__(self):
        return f"{self.id} - {self.marca_de_vehiculo} - {self.modelo_de_vehiculo} - {self.nacionalidad_de_fabricante}"
    
class Japones(models.Model):
    marca_de_vehiculo = models.CharField(max_length = 15)
    modelo_de_vehiculo = models.CharField(max_length = 15)
    motor = models.CharField(max_length = 20)
    descripcion_vehiculo = models.CharField(max_length = 100)
    nacionalidad_de_fabricante = models.CharField(max_length = 15)
    
    def __str__(self):
        return f"{self.id} - {self.marca_de_vehiculo} - {self.modelo_de_vehiculo} - {self.nacionalidad_de_fabricante}"
    
    

    

    

    

    







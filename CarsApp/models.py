from django.db import models

class vehiculos(models.Model):
    marca_de_vehiculo = models.CharField(max_length = 15)
    modelo_de_vehiculo = models.CharField(max_length = 15)
    motor = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 100)
    datos_del_dueño = models.CharField(max_length = 15)
    valor_vehiculo_usd = models.CharField(max_length = 30)


    def __str__(self):
        return f"{self.id} - {self.marca_de_vehiculo} - {self.modelo_de_vehiculo} - {self.valor_vehiculo_usd}"
    
    
    

    

    

    

    







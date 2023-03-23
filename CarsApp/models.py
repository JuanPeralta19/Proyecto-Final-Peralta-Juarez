from django.db import models
from django.contrib.auth.models import User
class vehiculos(models.Model):
    marca_de_vehiculo = models.CharField(max_length = 15)
    modelo_de_vehiculo = models.CharField(max_length = 15)
    motor = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 200)
    datos_del_dueño = models.CharField(max_length = 100)
    valor_vehiculo = models.CharField(max_length = 30)
    publicador = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name = "publicados")
    imagen = models.ImageField(upload_to="vehiculos", null=True, blank=True)

    @property
    def imagen_url(self):
        return self.imagen.url if self.imagen else ''

    def __str__(self):
        return f"{self.id} - {self.marca_de_vehiculo} - {self.modelo_de_vehiculo} - {self.valor_vehiculo}"
    
    
    

    

    

    

    







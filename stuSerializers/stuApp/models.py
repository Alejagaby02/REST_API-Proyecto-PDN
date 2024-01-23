from django.db import models

# Create your models here.
class Vuelo (models.Model):
    numero_vuelo= models.CharField(max_length=20)
    aereolinea = models.CharField(max_length=100)
    ciudad_destino = models.CharField(max_length=100)
    arrivo = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField()

class Pasajero (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    numero_telefono = models.CharField(max_length=15)

class Reservacion (models.Model):
    vuelo = models.OneToOneField(Vuelo, on_delete=models.CASCADE)
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE)

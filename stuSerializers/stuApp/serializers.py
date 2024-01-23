from rest_framework import serializers
from .models import Vuelo, Pasajero, Reservacion

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = '__all__'

class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'

class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'

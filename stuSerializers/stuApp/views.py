from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Vuelo, Pasajero, Reservacion
from .serializers import VueloSerializer, PasajeroSerializer, ReservacionSerializer

# Create your views here.

class Vuelo_list(APIView):
    def get(self,request):
        vuelo = Vuelo.objects.all()
        serializer = VueloSerializer(vuelo,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = VueloSerializer(data=request.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Vuelo_detail(APIView):
    def get_object(self,pk):
        try:
            return Vuelo.objects.get(pk=pk)
        except Vuelo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        vuelo = self.get_object(pk)
        serializer = VueloSerializer(vuelo)
        return Response(serializer.data)
    def put(self,request,pk):
        vuelo = self.get_object(pk)
        serializer = VueloSerializer(vuelo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        vuelo = self.get_object(pk)
        vuelo.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class Pasajero_list(APIView):
    def get(self, request):
        pasajeros = Pasajero.objects.all()
        serializer = PasajeroSerializer(pasajeros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PasajeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Pasajero_detail(APIView):
    def get_object(self, pk):
        try:
            return Pasajero.objects.get(pk=pk)
        except Pasajero.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        pasajero = self.get_object(pk)
        serializer = PasajeroSerializer(pasajero)
        return Response(serializer.data)

    def post(self, request, pk):
        pasajero = self.get_object(pk)
        serializer = PasajeroSerializer(pasajero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pasajero = self.get_object(pk)
        pasajero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Reservacion_list(APIView):
    def get(self, request):
        reservaciones = Reservacion.objects.all()
        serializer = ReservacionSerializer(reservaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Reservacion_detail(APIView):
    def get_object(self, pk):
        try:
            return Reservacion.objects.get(pk=pk)
        except Reservacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        reservacion = self.get_object(pk)
        serializer = ReservacionSerializer(reservacion)
        return Response(serializer.data)

    def put(self, request, pk):
        reservacion = self.get_object(pk)
        serializer = ReservacionSerializer(reservacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservacion = self.get_object(pk)
        reservacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

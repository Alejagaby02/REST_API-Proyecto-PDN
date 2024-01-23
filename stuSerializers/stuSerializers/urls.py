"""
URL configuration for stuSerializers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from stuApp.views import (Vuelo_list, Vuelo_detail, Pasajero_list, Pasajero_detail, Reservacion_list, Reservacion_detail)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Vuelo URLs
    path('vuelos/', Vuelo_list.as_view(), name='vuelo-list'),
    path('vuelos/<int:pk>/', Vuelo_detail.as_view(), name='vuelo-detail'),

    # Pasajero URLs
    path('pasajeros/', Pasajero_list.as_view(), name='pasajero-list'),
    path('pasajeros/<int:pk>/', Pasajero_detail.as_view(), name='pasajero-detail'),

    # Reservacion URLs
    path('reservaciones/', Reservacion_list.as_view(), name='reservacion-list'),
    path('reservaciones/<int:pk>/', Reservacion_detail.as_view(), name='reservacion-detail'),
]


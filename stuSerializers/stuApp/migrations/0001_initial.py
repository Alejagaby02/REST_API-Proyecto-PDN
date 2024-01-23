# Generated by Django 5.0.1 on 2024-01-23 00:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('numero_telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_vuelo', models.CharField(max_length=20)),
                ('aereolinea', models.CharField(max_length=100)),
                ('ciudad_destino', models.CharField(max_length=100)),
                ('arrivo', models.CharField(max_length=100)),
                ('fecha_salida', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasajero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stuApp.pasajero')),
                ('vuelo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stuApp.vuelo')),
            ],
        ),
    ]
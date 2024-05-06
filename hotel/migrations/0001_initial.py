# Generated by Django 5.0.4 on 2024-05-06 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('img_hotel', models.CharField(max_length=45, null=True)),
                ('descripcion', models.CharField(max_length=45)),
                ('fecha_disponibilidad', models.CharField(max_length=45)),
                ('n_habitaciones', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_habitacion', models.CharField(max_length=45)),
                ('fecha_inicio', models.CharField(max_length=45)),
                ('fecha_finalizacion', models.CharField(max_length=45)),
                ('precio', models.CharField(max_length=45)),
                ('ofertascol', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_habitacion', models.CharField(max_length=45)),
                ('capacidad_personas', models.CharField(max_length=45)),
                ('disponibilidad', models.CharField(max_length=45)),
                ('precio', models.CharField(max_length=45)),
                ('reserva_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.reservahotel')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='ofertas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.ofertas'),
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-07 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_hotel_ofertas_ofertas_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofertas',
            name='id_habitacion',
        ),
        migrations.AddField(
            model_name='ofertas',
            name='habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.habitaciones'),
        ),
    ]

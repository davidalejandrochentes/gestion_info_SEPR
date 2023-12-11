# Generated by Django 4.2.7 on 2023-11-25 23:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_sindical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asambleaafiliados',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
    ]

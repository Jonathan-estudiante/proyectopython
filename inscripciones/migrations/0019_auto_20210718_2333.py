# Generated by Django 3.2.5 on 2021-07-19 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0018_auto_20210718_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='apellido_estudiante',
        ),
        migrations.RemoveField(
            model_name='inscripciones',
            name='nombre_estudiante',
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='fecha_registro_curso',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 18, 23, 33, 40, 292236)),
        ),
    ]

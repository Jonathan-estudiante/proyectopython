# Generated by Django 3.2.5 on 2021-07-17 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='contenido',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='curso',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 1, 19, 49, 178402)),
        ),
    ]
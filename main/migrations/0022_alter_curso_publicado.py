# Generated by Django 3.2.5 on 2021-07-18 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 19, 33, 44, 170730)),
        ),
    ]

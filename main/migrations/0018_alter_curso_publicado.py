# Generated by Django 3.2.5 on 2021-07-17 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 15, 57, 44, 428743)),
        ),
    ]
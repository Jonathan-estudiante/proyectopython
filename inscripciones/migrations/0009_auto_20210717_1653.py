# Generated by Django 3.2.5 on 2021-07-17 21:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inscripciones', '0008_auto_20210717_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripciones',
            name='user',
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscripciones',
            name='fecha_registro_curso',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 16, 51, 41, 737344)),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-16 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210715_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 16, 16, 58, 40, 896534)),
        ),
    ]

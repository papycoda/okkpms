# Generated by Django 2.2.6 on 2020-06-09 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200609_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 13, 43, 27, 172458), verbose_name='last login'),
        ),
    ]

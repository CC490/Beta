# Generated by Django 2.2b1 on 2019-03-01 01:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0009_auto_20190228_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmodel',
            name='conRecDate',
            field=models.DateField(default=datetime.date(2019, 3, 1)),
        ),
    ]

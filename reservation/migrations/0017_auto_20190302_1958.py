# Generated by Django 2.2b1 on 2019-03-03 00:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0016_auto_20190302_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisereservationmodel',
            name='dateEnd',
            field=models.DateField(default=datetime.datetime(2019, 3, 3, 0, 58, 7, 298341, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='revisereservationmodel',
            name='dateStart',
            field=models.DateField(default=datetime.datetime(2019, 3, 3, 0, 58, 7, 298341, tzinfo=utc)),
        ),
    ]

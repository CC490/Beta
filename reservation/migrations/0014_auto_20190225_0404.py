# Generated by Django 2.1.2 on 2019-02-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0013_auto_20190225_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisereservation',
            name='district',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='revisereservation',
            name='lunch',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='revisereservation',
            name='sayNo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='revisereservation',
            name='slowPay',
            field=models.BooleanField(default=False),
        ),
    ]

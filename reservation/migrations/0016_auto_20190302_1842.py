# Generated by Django 2.2b1 on 2019-03-02 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0015_auto_20190225_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revisereservationmodel',
            old_name='zip',
            new_name='zipCode',
        ),
    ]

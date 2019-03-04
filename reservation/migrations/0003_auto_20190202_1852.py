# Generated by Django 2.1.2 on 2019-02-02 23:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20190127_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revisereservation',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='revisereservation',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='revisereservation',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='revisereservation',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='revisereservation',
            name='title',
        ),
        migrations.AddField(
            model_name='revisereservation',
            name='fax',
            field=models.CharField(default=django.utils.timezone.now, max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='revisereservation',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='revisereservation',
            name='progLength',
            field=models.CharField(default=django.utils.timezone.now, max_length=24),
            preserve_default=False,
        ),
    ]

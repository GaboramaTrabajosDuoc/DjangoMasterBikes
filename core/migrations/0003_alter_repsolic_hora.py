# Generated by Django 4.0.4 on 2022-07-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_repsolic_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repsolic',
            name='Hora',
            field=models.CharField(max_length=300, verbose_name='Hora de atencion'),
        ),
    ]

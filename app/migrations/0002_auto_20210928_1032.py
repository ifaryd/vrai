# Generated by Django 2.2.14 on 2021-09-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0016_alter_booking_adults_alter_booking_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adults',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='children',
            field=models.IntegerField(),
        ),
    ]

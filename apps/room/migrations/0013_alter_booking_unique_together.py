# Generated by Django 5.0.2 on 2024-02-20 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0012_alter_booking_adults_alter_booking_children'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('room', 'check_in', 'check_out')},
        ),
    ]

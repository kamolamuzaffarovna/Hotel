# Generated by Django 5.0.2 on 2024-02-22 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0013_alter_booking_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
    ]

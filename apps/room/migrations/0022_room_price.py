# Generated by Django 5.0.2 on 2024-02-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0021_alter_room_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

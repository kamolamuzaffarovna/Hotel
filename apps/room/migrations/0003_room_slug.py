# Generated by Django 5.0.2 on 2024-02-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_remove_room_footer_image_footerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]

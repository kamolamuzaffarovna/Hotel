# Generated by Django 5.0.2 on 2024-02-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_remove_information_image_information_footer_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, max_length=221, null=True),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-24 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_blogcommentlike_author_blogcommentlike_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcommentlike',
            old_name='user',
            new_name='author',
        ),
    ]
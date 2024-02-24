# Generated by Django 5.0.2 on 2024-02-24 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcommentlike',
            name='blog',
        ),
        migrations.AddField(
            model_name='blogcommentlike',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]

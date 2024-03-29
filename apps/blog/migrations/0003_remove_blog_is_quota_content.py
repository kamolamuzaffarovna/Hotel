# Generated by Django 5.0.2 on 2024-02-15 02:59

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='is_quota',
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('is_quota', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='blog.blog')),
            ],
        ),
    ]

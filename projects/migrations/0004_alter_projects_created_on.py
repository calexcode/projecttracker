# Generated by Django 4.0.5 on 2022-06-30 03:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_projects_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

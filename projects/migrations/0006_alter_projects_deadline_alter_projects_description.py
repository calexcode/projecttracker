# Generated by Django 4.0.5 on 2022-06-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_projects_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='deadline',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]

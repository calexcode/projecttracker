# Generated by Django 4.0.5 on 2022-06-30 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projects_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]

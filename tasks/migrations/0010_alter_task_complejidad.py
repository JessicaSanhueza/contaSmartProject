# Generated by Django 4.1.1 on 2022-11-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_rename_description_task_complejidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complejidad',
            field=models.IntegerField(choices=[(1, 'Baja'), (2, 'Media'), (3, 'Alta')]),
        ),
    ]
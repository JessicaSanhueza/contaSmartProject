# Generated by Django 4.1.1 on 2022-11-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_solicitud_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]

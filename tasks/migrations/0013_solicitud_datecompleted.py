# Generated by Django 4.1.1 on 2022-11-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_solicitud_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

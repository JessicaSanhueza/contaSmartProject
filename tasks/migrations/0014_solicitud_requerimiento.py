# Generated by Django 4.1.1 on 2022-11-21 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_solicitud_datecompleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='requerimiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-01 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_subcategoria_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='subcategoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.subcategoria'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-01 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_area_subcategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasks.area'),
            preserve_default=False,
        ),
    ]
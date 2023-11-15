# Generated by Django 4.2.4 on 2023-11-15 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_app', '0003_alter_visitantes_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitantes',
            name='empleado',
            field=models.ForeignKey(limit_choices_to={'area': models.F('area_id')}, on_delete=django.db.models.deletion.CASCADE, to='edificio_app.empleado'),
        ),
    ]

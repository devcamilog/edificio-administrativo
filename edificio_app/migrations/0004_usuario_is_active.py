# Generated by Django 4.2.4 on 2023-11-24 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_app', '0003_remove_usuario_usuario_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

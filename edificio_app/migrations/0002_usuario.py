# Generated by Django 4.2.4 on 2023-11-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de Usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('nombres', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administracion', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
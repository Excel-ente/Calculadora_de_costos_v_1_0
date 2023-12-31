# Generated by Django 4.2.2 on 2023-08-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DESCRIPCION', models.CharField(max_length=120)),
                ('USER', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias Recetas',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODIGO', models.CharField(max_length=120)),
                ('NOMBRES', models.CharField(blank=True, max_length=120, null=True)),
                ('EMAIL', models.EmailField(blank=True, max_length=254, null=True)),
                ('TELEFONO', models.CharField(max_length=120)),
                ('USER', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False, verbose_name='ACTIVO')),
                ('NOMBRE_EMPRESA', models.CharField(blank=True, max_length=120, null=True)),
                ('DIRECCION', models.CharField(blank=True, max_length=255, null=True)),
                ('TELEFONO', models.CharField(blank=True, max_length=255, null=True)),
                ('EMAIL', models.CharField(blank=True, max_length=255, null=True)),
                ('LOGO', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('USER', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Mis Datos',
                'verbose_name_plural': 'Mis Datos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMPRESA', models.CharField(max_length=120)),
                ('NOMBRE', models.CharField(max_length=120)),
                ('DIRECCION', models.CharField(blank=True, max_length=120, null=True)),
                ('EMAIL', models.EmailField(blank=True, max_length=254, null=True)),
                ('TELEFONO', models.CharField(max_length=120)),
                ('USER', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]

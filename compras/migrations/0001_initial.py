# Generated by Django 4.2.2 on 2023-08-27 07:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articulosCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, default=1, max_digits=20)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Precio Total')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos de la compra',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('FECHA', models.DateField(default=datetime.date.today)),
                ('CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('ESTADO', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Controlada', 'Controlada')], default='Pendiente', max_length=50)),
                ('MEDIO_DE_PAGO', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Cuenta Corriente', 'Cuenta Corriente')], default='Efectivo', max_length=50)),
                ('DETALLES_ADICIONALES', models.TextField(blank=True, null=True)),
                ('COSTO_FINAL', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=22, null=True)),
                ('USER', models.CharField(blank=True, max_length=120, null=True)),
                ('ARTICULOS', models.ManyToManyField(related_name='compras_insumo', through='compras.articulosCompra', to='inventario.producto')),
                ('PROVEEDOR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compras_proveedor', to='administracion.proveedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras de insumos',
            },
        ),
        migrations.AddField(
            model_name='articuloscompra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.compra'),
        ),
        migrations.AddField(
            model_name='articuloscompra',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos_compra', to='inventario.producto'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-27 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica', '0005_alter_orden_articulos'),
        ('compras', '0005_articuloscompra_actualizar_inventario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumoscompra',
            name='insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insumos', to='fabrica.insumo', unique=True),
        ),
        migrations.AlterField(
            model_name='insumoscompra',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Precio Unitario'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gastosAdicionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRODUCTO', models.CharField(max_length=255)),
                ('USER', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
    ]
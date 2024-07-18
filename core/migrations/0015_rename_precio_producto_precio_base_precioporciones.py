# Generated by Django 5.0.6 on 2024-07-16 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_producto_precio_base_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='precio_base',
        ),
        migrations.CreateModel(
            name='PrecioPorciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porciones', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precios_porciones', to='core.producto')),
            ],
        ),
    ]

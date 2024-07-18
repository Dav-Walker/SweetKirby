# Generated by Django 5.0.6 on 2024-07-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_categoria_rename_stock_producto_cantidad_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='precio_base',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_porciones',
            field=models.JSONField(default=dict),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-16 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_precio_producto_precio_base_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio_base',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_porciones',
        ),
    ]

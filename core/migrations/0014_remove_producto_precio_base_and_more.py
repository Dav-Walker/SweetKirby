# Generated by Django 5.0.6 on 2024-07-16 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_producto_precio_producto_precio_base_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='precio_base',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_porciones',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

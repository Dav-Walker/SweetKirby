# Generated by Django 5.0.6 on 2024-05-31 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_producto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
    ]

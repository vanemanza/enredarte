# Generated by Django 2.2.3 on 2019-08-27 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumoscompra',
            name='precio_compra',
            field=models.PositiveIntegerField(default=100, help_text='Precio unitario'),
            preserve_default=False,
        ),
    ]

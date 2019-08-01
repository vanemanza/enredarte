# Generated by Django 2.2.3 on 2019-07-31 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('creado', 'Creado'), ('pagado', 'Pagado'), ('entregado', 'Entregado')], default='creado', max_length=64),
        ),
    ]

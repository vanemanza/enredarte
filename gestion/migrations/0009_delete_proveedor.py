# Generated by Django 2.2.3 on 2019-07-23 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20190723_1407'),
        ('gestion', '0008_auto_20190722_1510'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Proveedor',
        ),
    ]

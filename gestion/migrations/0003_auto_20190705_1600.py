# Generated by Django 2.2.3 on 2019-07-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20190704_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['provincia']},
        ),
        migrations.AddField(
            model_name='localidad',
            name='cod_postal',
            field=models.CharField(default=5921, max_length=10, verbose_name='Codigo Postal'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.3 on 2019-11-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0015_auto_20191126_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='productos/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]

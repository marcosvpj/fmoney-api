# Generated by Django 2.0 on 2018-05-20 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='date',
            field=models.DateField(verbose_name='data de compra'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='note',
            field=models.CharField(blank=True, max_length=255, verbose_name='notas'),
        ),
    ]

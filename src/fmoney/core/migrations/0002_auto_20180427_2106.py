# Generated by Django 2.0 on 2018-04-28 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'transação', 'verbose_name_plural': 'transações'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(blank=True, max_length=255, verbose_name='metodo de pagamento'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='place',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='local'),
        ),
    ]
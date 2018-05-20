from django.db import models

# Create your models here.


class Transaction(models.Model):
    title = models.CharField('titulo', max_length=255)
    value = models.DecimalField('valor', max_digits=10, decimal_places=2)
    due_date = models.DateField('data de vencimento')
    payment_method = models.CharField('metodo de pagamento', max_length=255, blank=True)
    place = models.CharField('local', max_length=255, blank=True, null=True, default=None)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name = 'transação'
        verbose_name_plural = 'transações'

    def __str__(self):
        return self.title


class Asset(models.Model):
    name = models.CharField('nome', max_length=255)
    date = models.DateField('data de compra')
    symbol = models.CharField('simbolo', max_length=255)
    shares = models.DecimalField('cotas', max_digits=10, decimal_places=2)
    commission = models.DecimalField('taxas', max_digits=10, decimal_places=2)
    type = models.CharField('operação', max_length=255)
    note = models.CharField('notas', max_length=255, blank=True)

    class Meta:
        verbose_name = 'ativo'
        verbose_name_plural = 'ativos'

    def __str__(self):
        return self.symbol

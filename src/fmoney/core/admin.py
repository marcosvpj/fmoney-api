from django.contrib import admin
from fmoney.core.models import Transaction
from fmoney.core.models import Asset
# Register your models here.


class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ['due_date', 'title', 'value']

class AssetModelAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'name', 'shares']

admin.site.register(Transaction, TransactionModelAdmin)
admin.site.register(Asset, AssetModelAdmin)
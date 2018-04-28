from django.contrib import admin
from fmoney.core.models import Transaction
# Register your models here.


class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ['due_date', 'title', 'value']

admin.site.register(Transaction, TransactionModelAdmin)
from django.contrib import admin
from .models import Transaction
# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ['owner','made_on']
    list_display = ('owner', 'made_on','transaction_ref','charged_amount','transaction_id')
    search_fields = ['name', 'email']


admin.site.register(Transaction,TransactionAdmin)
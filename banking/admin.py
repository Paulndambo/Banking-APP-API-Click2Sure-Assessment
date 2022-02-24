from django.contrib import admin
from . models import *
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
from django.contrib.auth.models import User
# Register your models here.
class AccountResource(resources.ModelResource):
    user = Field()
    class Meta:
        model = Account
        fields = ("user", "account_name", "account_number", "bank_name", "balance")

    def dehydrate_user(self, obj):
        return obj.user.username

class AccountAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = AccountResource
    list_display = ("user", "account_name", "account_number", "bank_name", "balance")

admin.site.register(Account, AccountAdmin)



class BankTransactionResource(resources.ModelResource):
    user = Field()
    class Meta:
        model = BankTransaction
        fields = ('user', 'account', 'transaction_type', 'amount', 'transaction_date')
        

    def dehydrate_user(self, obj):
        return obj.user.username

class BankTransactionAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = BankTransactionResource
    list_display = ["user", "account", "transaction_type", "amount"]
    list_filter = ["transaction_type"]
    search_fields = ["account",]
    

admin.site.register(BankTransaction, BankTransactionAdmin)
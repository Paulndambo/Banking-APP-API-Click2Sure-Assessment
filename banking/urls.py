
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *

router = DefaultRouter()
router.register("bank-accounts", BankAccountViewSet, basename="bank-accounts")

urlpatterns = [
    path("", include(router.urls)),
    #path("all-accounts/", ListBankAccounts.as_view(), name="all-accounts"),
    #path("create-bank-account/", CreateAccount.as_view(), name="create-bank-account"),
    path("transact/", MakeBankTransaction.as_view(), name="transact"),
    path("user-transactions/<int:user>/", UserTransactionsList.as_view(), name="user-transactions"),
    path("user-bank-accounts/", UserBankAccountsList.as_view(), name="user-bank-accounts"),
    path("account-transactions/", BankAccountTransactions.as_view(), name="account-transactions"),
    path("all-bank-transactions/", AllBankTransactions.as_view(), name="all-bank-transactions"),
]

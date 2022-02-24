from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Bank(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.CharField(max_length=200)

    def __str__(self):
        return self.title

ACCOUNT_TYPES = (
    ("Savings", "Savings"),
    ("Credit", "Credit"),
)

TRANSACTION_TYPES = (
    ("Deposit", "Deposit"),
    ("Withdraw", "Withdraw"),
)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=200, default="Test Bank")
    account_number = models.CharField(max_length=200, primary_key=True)
    account_name = models.CharField(max_length=200, default="Test Account")
    account_type = models.CharField(max_length=200, choices=ACCOUNT_TYPES)
    balance = models.FloatField(default=0)
    date_created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.account_number

class BankTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=200, choices=TRANSACTION_TYPES)
    amount = models.FloatField(default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


    

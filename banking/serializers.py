from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . models import *


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = BankTransaction
        fields = "__all__"


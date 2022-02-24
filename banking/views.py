from django.shortcuts import render
from . models import Account, BankTransaction
from . serializers import BankAccountSerializer, TransactionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.db import connection
cursor = connection.cursor()


# Create your views here.
#CRUD For Bank Accounts Only Accessible To Admin Users Only
class BankAccountViewSet(ModelViewSet):
    serializer_class = BankAccountSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = Account.objects.all()

# Returns Bank Transactions of A Specific User By ID
class UserTransactionsList(generics.GenericAPIView):
    serializer_class = TransactionSerializer
    #permission_classes = (permissions.IsAdminUser,)
    
    def get(self, request, format=None, **kwargs):
        transactions = BankTransaction.objects.filter(user=kwargs['user'])
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
#Returns All Bank Transactions For Authenticated User
class BankAccountTransactions(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
       return BankTransaction.objects.filter(user=self.request.user)[:10]

#Returns All Bank Accounts and Balances For Authenticated User
#The View User By Non-Admin Users To Create Bank Accounts
class UserBankAccountsList(generics.ListCreateAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
       return Account.objects.filter(user=self.request.user)

#Returns All Bank Transactions
class AllBankTransactions(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        return BankTransaction.objects.all()


#Where Bank Transactions Are Created
class MakeBankTransaction(generics.GenericAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():

            acc_number = str(serializer.validated_data['account'])
            account = Account.objects.filter(account_number=acc_number)
            balance = account.values()[0]['balance']
            account_type = account.values()[0]['account_type']
            amount = serializer.validated_data["amount"]

            if serializer.validated_data["transaction_type"] == "Deposit":
                total_balance = amount + balance
                str_balance = str(total_balance)
                
                def update_balance():
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE banking_account SET balance = %s WHERE account_number=%s ", [str_balance, acc_number])
                update_balance()


                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif serializer.validated_data["transaction_type"] == "Withdraw":
                if account_type == "Savings":
                    if balance - amount >= 50:
                        total_balance = balance - amount
                        str_balance = str(total_balance)

                        def update_balance():
                            with connection.cursor() as cursor:
                                cursor.execute("UPDATE banking_account SET balance = %s WHERE account_number= %s ", [str_balance, acc_number])
                        update_balance()

                        
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"failed": "You Acount Should Always Have R50 or Above"}, status=status.HTTP_400_BAD_REQUEST)
                elif account_type == "Credit":
                    if balance - amount >= -20000:
                        total_balance = balance - amount
                        str_balance = str(total_balance)

                        def update_balance():
                            with connection.cursor() as cursor:
                                cursor.execute("UPDATE banking_account SET balance = %s WHERE account_number= %s ", [str_balance, acc_number])
                        update_balance()


                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"failed": "You have reached your maximum credit"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

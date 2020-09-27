from rest_framework import serializers

from budget.models import Account, Transaction, CATEGORY_CHOICES


class AccountsSerializer(serializers.ModelSerializer):
    account = serializers.CharField(max_length=32)
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)
    description = serializers.CharField(max_length=100)
    class Meta:
        model = Account
        fields = ['account', 'category', 'description']


class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.CharField(max_length=32)
    amount = serializers.IntegerField()
    date = serializers.DateField()
    owner = serializers.CharField(max_length=50)

    class Meta:
        model = Transaction
        fields = ['account', 'amount', 'date']


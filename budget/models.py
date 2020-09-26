from django.db import models

CATEGORY_CHOICES = (
    (0, 'income'),
    (1, 'expense'),
)

class Account(models.Model):
    account = models.CharField(max_length=32, unique=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.account

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    amount = models.PositiveIntegerField()
    date = models.DateField()
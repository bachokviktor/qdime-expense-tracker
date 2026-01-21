from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Transaction(models.Model):
    TYPE_INCOME = "IN"
    TYPE_EXPENSE = "EX"

    TRANSACTION_TYPE = {
        TYPE_EXPENSE: "Expense",
        TYPE_INCOME: "Income"
    }

    EXPENSE_CATEGORIES = {
        "Rent": "Rent",
        "Transportation": "Transportation",
        "Utilities": "Utilities",
        "Food": "Food",
        "Healthcare": "Healthcare",
        "Entertainment": "Entertainment",
        "Other": "Other"
    }

    INCOME_CATEGORIES = {
        "Salary": "Salary",
        "Gift": "Gift",
        "Other": "Other"
    }

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    type = models.CharField(choices=TRANSACTION_TYPE)
    category = models.CharField(choices=EXPENSE_CATEGORIES|INCOME_CATEGORIES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.type}){self.amount}: {self.category}"

    class Meta:
        ordering = ["-date"]

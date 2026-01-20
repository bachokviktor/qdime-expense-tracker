from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Expense(models.Model):
    EXPENSE_CATEGORIES = {
        "Rent": "Rent",
        "Transportation": "Transportation",
        "Utilities": "Utilities",
        "Food": "Food",
        "Healthcare": "Healthcare",
        "Entertainment": "Entertainment",
        "Other": "Other"
    }

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.CharField(choices=EXPENSE_CATEGORIES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"-{self.amount}: {self.category}"

    class Meta:
        ordering = ["date"]

class Income(models.Model):
    INCOME_CATEGORIES = {
        "Salary": "Salary",
        "Other": "Other"
    }

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.CharField(choices=INCOME_CATEGORIES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"+{self.amount}: {self.category}"

    class Meta:
        ordering = ["date"]

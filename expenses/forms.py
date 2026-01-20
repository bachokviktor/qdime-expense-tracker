from django.forms import ModelForm

from . import models


class ExpenseForm(ModelForm):
    class Meta:
        model = models.Expense
        fields = ["amount", "category"]


class IncomeForm(ModelForm):
    class Meta:
        model = models.Income
        fields = ["amount", "category"]

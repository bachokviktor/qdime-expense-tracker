from django.forms import ModelForm

from . import models

class ExpenseForm(ModelForm):
    class Meta:
        model = models.Transaction
        fields = ["amount", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["category"].choices = models.Transaction.EXPENSE_CATEGORIES


class IncomeForm(ModelForm):
    class Meta:
        model = models.Transaction
        fields = ["amount", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["category"].choices = models.Transaction.INCOME_CATEGORIES

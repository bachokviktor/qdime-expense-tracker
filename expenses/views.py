from django.shortcuts import render
from django.views import View


# Create your views here.
class ExpensesView(View):
    template_name = "expenses/expenses.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

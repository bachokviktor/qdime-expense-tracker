from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import forms, models


# Create your views here.
class AddExpenseView(LoginRequiredMixin, View):
    login_url = "users:login"
    template_name = "expenses/add_expense.html"

    def get(self, request, *args, **kwargs):
        form = forms.ExpenseForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = forms.ExpenseForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"form": form})


class EditExpenseView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "users:login"
    template_name = "expenses/edit_expense.html"

    def test_func(self):
        instance = models.Expense.objects.get(id=self.kwargs["expense_id"])

        return self.request.user == instance.user

    def get(self, request, expense_id, *args, **kwargs):
        instance = models.Expense.objects.get(id=expense_id)
        form = forms.ExpenseForm(instance=instance)

        return render(request, self.template_name, {"form": form, "expense_id": expense_id})

    def post(self, request, expense_id, *args, **kwargs):
        instance = models.Expense.objects.get(id=expense_id)
        form = forms.ExpenseForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"form": form, "expense_id": expense_id})


class DeleteExpenseView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "users:login"

    def test_func(self):
        instance = models.Expense.objects.get(id=self.kwargs["expense_id"])

        return self.request.user == instance.user

    def get(self, request, expense_id, *args, **kwargs):
        instance = models.Expense.objects.get(id=expense_id)
        instance.delete()

        return redirect("users:profile")


class AddIncomeView(LoginRequiredMixin, View):
    login_url = "users:login"
    template_name = "expenses/add_income.html"

    def get(self, request, *args, **kwargs):
        form = forms.IncomeForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = forms.IncomeForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"form": form})


class EditIncomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "users:login"
    template_name = "expenses/edit_income.html"

    def test_func(self):
        instance = models.Income.objects.get(id=self.kwargs["income_id"])

        return self.request.user == instance.user

    def get(self, request, income_id, *args, **kwargs):
        instance = models.Income.objects.get(id=income_id)
        form = forms.IncomeForm(instance=instance)

        return render(request, self.template_name, {"form": form, "income_id": income_id})

    def post(self, request, income_id, *args, **kwargs):
        instance = models.Income.objects.get(id=income_id)
        form = forms.IncomeForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"form": form, "income_id": income_id})


class DeleteIncomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "users:login"

    def test_func(self):
        instance = models.Income.objects.get(id=self.kwargs["income_id"])

        return self.request.user == instance.user

    def get(self, request, income_id, *args, **kwargs):
        instance = models.Income.objects.get(id=income_id)
        instance.delete()

        return redirect("users:profile")

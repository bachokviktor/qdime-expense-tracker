from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import forms, models


# Create your views here.
class AddExpenseView(LoginRequiredMixin, View):
    login_url = "users:login"
    template_name = "expenses/add.html"
    instance_type = "expense"

    def get(self, request, *args, **kwargs):
        form = forms.ExpenseForm()

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form})

    def post(self, request, *args, **kwargs):
        form = forms.ExpenseForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.type = models.Transaction.TYPE_EXPENSE
            instance.user = request.user
            instance.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form})


class EditExpenseView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "users:login"
    template_name = "expenses/edit.html"
    instance_type = "expense"

    def test_func(self):
        instance = models.Transaction.objects.get(id=self.kwargs["transaction_id"])

        return self.request.user == instance.user

    def get(self, request, transaction_id, *args, **kwargs):
        instance = models.Transaction.objects.get(id=transaction_id)
        form = forms.ExpenseForm(instance=instance)

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form, "transaction_id": transaction_id})

    def post(self, request, transaction_id, *args, **kwargs):
        instance = models.Transaction.objects.get(id=transaction_id)
        form = forms.ExpenseForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form, "transaction_id": transaction_id})


class AddIncomeView(LoginRequiredMixin, View):
    login_url = "users:login"
    template_name = "expenses/add.html"
    instance_type = "income"

    def get(self, request, *args, **kwargs):
        form = forms.IncomeForm()

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form})

    def post(self, request, *args, **kwargs):
        form = forms.IncomeForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.type = models.Transaction.TYPE_INCOME
            instance.user = request.user
            instance.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form})


class EditIncomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "users:login"
    template_name = "expenses/edit.html"
    instance_type = "income"

    def test_func(self):
        instance = models.Transaction.objects.get(id=self.kwargs["transaction_id"])

        return self.request.user == instance.user

    def get(self, request, transaction_id, *args, **kwargs):
        instance = models.Transaction.objects.get(id=transaction_id)
        form = forms.IncomeForm(instance=instance)

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form, "transaction_id": transaction_id})

    def post(self, request, transaction_id, *args, **kwargs):
        instance = models.Transaction.objects.get(id=transaction_id)
        form = forms.IncomeForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            return redirect("users:profile")

        return render(request, self.template_name, {"instance_type": self.instance_type, "form": form, "transaction_id": transaction_id})


class DeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = "users:login"

    def test_func(self):
        instance = models.Transaction.objects.get(id=self.kwargs["transaction_id"])

        return self.request.user == instance.user

    def get(self, request, transaction_id, *args, **kwargs):
        instance = models.Transaction.objects.get(id=transaction_id)
        instance.delete()

        return redirect("users:profile")

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce

from expenses.models import Transaction


# Create your views here.
class ProfileView(LoginRequiredMixin, View):
    login_url = "users:login"
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        user_transactions = Transaction.objects.filter(user=request.user)

        user_income = user_transactions.filter(type="IN").aggregate(sum=Coalesce(Sum("amount", output_field=FloatField()), float(0)))
        user_expense = user_transactions.filter(type="EX").aggregate(sum=Coalesce(Sum("amount", output_field=FloatField()), float(0)))

        user_balance = user_income["sum"] - user_expense["sum"]

        category_values = user_transactions.filter(type="EX").values("category").annotate(sum=Sum("amount"))

        category_labels = [i["category"] for i in category_values]
        category_data = [float(i["sum"]) for i in category_values]

        return render(request, self.template_name, {"user_transactions": user_transactions, "user_balance": user_balance, "category_labels": category_labels, "category_data": category_data})


class LoginView(View):
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.POST.get("next")

            if next_url:
                return redirect(next_url)
            else:
                return redirect("core:home")

        return render(request, self.template_name, {"form": form})


class RegistrationView(View):
    template_name = "users/registration.html"

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()

        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            login(request, form.save())

            return redirect("core:home")

        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)

        return redirect("core:home")

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from expenses.models import Expense, Income


# Create your views here.
class ProfileView(LoginRequiredMixin, View):
    login_url = "users:login"
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        user_expenses = Expense.objects.filter(user=request.user).reverse()
        user_incomes = Income.objects.filter(user=request.user).reverse()
        
        return render(request, self.template_name, {"user_expenses": user_expenses, "user_incomes": user_incomes})


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

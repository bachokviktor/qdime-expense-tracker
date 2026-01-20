from django.urls import path

from . import views


app_name = "expenses"

urlpatterns = [
    path("add/expense/", views.AddExpenseView.as_view(), name="add_expense"),
    path("edit/expense/<int:expense_id>/", views.EditExpenseView.as_view(), name="edit_expense"),
    path("delete/expense/<int:expense_id>/", views.DeleteExpenseView.as_view(), name="delete_expense"),
    path("add/income/", views.AddIncomeView.as_view(), name="add_income"),
    path("edit/income/<int:income_id>/", views.EditIncomeView.as_view(), name="edit_income"),
    path("delete/income/<int:income_id>/", views.DeleteIncomeView.as_view(), name="delete_income")
]

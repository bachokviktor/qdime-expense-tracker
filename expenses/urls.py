from django.urls import path

from . import views


app_name = "expenses"

urlpatterns = [
    path("add/expense/", views.AddExpenseView.as_view(), name="add_expense"),
    path("edit/expense/<int:transaction_id>/", views.EditExpenseView.as_view(), name="edit_expense"),
    path("add/income/", views.AddIncomeView.as_view(), name="add_income"),
    path("edit/income/<int:transaction_id>/", views.EditIncomeView.as_view(), name="edit_income"),
    path("delete/<int:transaction_id>/", views.DeleteView.as_view(), name="delete")
]

from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm


def my_expense(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'cost/expense.html', context)


def add_expense(request):
    form = ExpenseForm
    return render(request, 'cost/add_expense.html', {'form': form})
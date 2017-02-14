from django.shortcuts import render
from .models import Expense


def my_expense(request):
    expenses = Expense.objects.all()
    print(expenses)
    context = {'expenses': expenses}
    return render(request, 'cost/expense.html', context)
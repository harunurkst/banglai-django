from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.my_expense, name='cost-list'),
    path('add/', views.add_expense, name='add-expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit-expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete-expense'),

]

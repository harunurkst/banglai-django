from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.my_expense, name='cost-list'),
    url(r'^add/$', views.add_expense, name='add-expense'),
    url(r'^edit/(?P<expense_id>[0-9]+)/$', views.edit_expense, name='edit-expense'),
    url(r'^delete/(?P<expense_id>[0-9]+)/$', views.delete_expense, name='delete-expense'),

]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.my_expense, name='cost-list'),
    url(r'^add/$', views.add_expense, name='add-expense'),

]

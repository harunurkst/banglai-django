from django.urls import path
from . import views

urlpatterns = [
    path('districts/', views.district_list, name='districts'),

]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^districts/', views.district_list, name='districts'),

]

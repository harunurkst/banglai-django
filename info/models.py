from django.db import models
from inventory.models import Stock 

class Shop(models.Model):
    name = models.CharField(max_length=45)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='shop_set')
     

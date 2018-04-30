from django.db import models
#from info.models import Shop

class Stock(models.Model):
    item = models.CharField(max_length=45)
    shop = models.ForeignKey('info.Shop', on_delete=models.CASCADE, related_name='stock_set')

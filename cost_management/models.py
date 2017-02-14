from django.db import models


class Expense(models.Model):
    amount = models.IntegerField()
    purpose = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purpose

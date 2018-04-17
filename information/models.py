from django.db import models


class Divisions(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    area = models.IntegerField()

    def __str__(self):
        return self.name


class Districts(models.Model):
    name = models.CharField(max_length=50)
    education_rate = models.IntegerField()
    population_density = models.IntegerField(blank=True, null=True)
    visited = models.BooleanField(default=False)
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


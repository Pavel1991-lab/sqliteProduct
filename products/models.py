
from django.db import models



class Product(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    cost = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт',
        verbose_name_plural = 'продукты'

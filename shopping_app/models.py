from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

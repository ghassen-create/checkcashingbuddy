from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    commission = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

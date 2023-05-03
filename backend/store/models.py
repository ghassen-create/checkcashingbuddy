from django.db import models

from customer.models import Customer


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_created_at(self):
        return f"{self.created_at.date()} {self.created_at.strftime('%H:%M:%S')}"

    @property
    def get_updated_at(self):
        return f"{self.updated_at.date()} {self.updated_at.strftime('%H:%M:%S')}"

    def __str__(self):
        return self.name


class StoreCustomer(models.Model):
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    @property
    def store_name(self):
        return self.store.name if self.store else ""

    @property
    def customer_name(self):
        return self.customer.name if self.customer else ""

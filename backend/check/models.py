from auditlog.registry import auditlog
from django.db import models

from customer.models import Customer

from store.models import Store


# Create your models here.
class Check(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, related_name='checks')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=3)
    front_image = models.ImageField(upload_to='check_images/')
    back_image = models.ImageField(upload_to='check_images/')
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

    @property
    def customer_name(self):
        return self.customer.name if self.customer else ""

    @property
    def store_name(self):
        return self.store.name if self.store else ""

    @property
    def net_payment(self):
        if self.commission:
            return round(float(self.amount) - ((float(self.commission) * float(self.amount)) / 100), 2)
        else:
            return round(float(self.amount) - ((3 * float(self.amount)) / 100), 2)

    @property
    def get_created_at(self):
        return f"{self.created_at.date()} {self.created_at.strftime('%H:%M:%S')}"

    @property
    def get_updated_at(self):
        return f"{self.updated_at.date()} {self.updated_at.strftime('%H:%M:%S')}"


auditlog.register(Check)

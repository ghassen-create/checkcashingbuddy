from auditlog.registry import auditlog
from django.db import models

from customer.models import Customer


# Create your models here.
class Check(models.Model):
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL, related_name="checks"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True, default=6
    )
    front_image = models.ImageField(upload_to="check_images/")
    back_image = models.ImageField(upload_to="check_images/")
    scanned_by_admin = models.BooleanField(default=False)
    scanned_by_store = models.BooleanField(default=False)

    def __str__(self):
        return str(self.amount)

    @property
    def customer_username(self):
        return self.customer.name if self.customer else ""

    @property
    def net_payment(self):
        if self.commission:
            return round(
                float(self.amount)
                - ((float(self.commission) * float(self.amount)) / 100),
                2,
            )
        else:
            return round(float(self.amount) - ((6 * float(self.amount)) / 100), 2)


auditlog.register(Check)

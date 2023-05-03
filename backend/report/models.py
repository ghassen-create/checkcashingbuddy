from check.models import Check
from django.db import models


# Create your models here.
class Report(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=5, decimal_places=2)
    cheque = models.ForeignKey(
        Check, null=True, on_delete=models.SET_NULL, related_name="reports"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def net_payment(self):
        return self.cheque.net_payment if self.cheque else ""

    @property
    def get_created_at(self):
        return f"{self.created_at.date()} {self.created_at.strftime('%H:%M:%S')}"

    def __str__(self):
        return f"{self.cheque.customer} report"

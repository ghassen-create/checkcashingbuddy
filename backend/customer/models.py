from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=80)
    address_1 = models.CharField(max_length=100, null=True, blank=True)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
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


class Avatar(models.Model):
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True, default=None)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_created_at(self):
        return f"{self.created_at.date()} {self.created_at.strftime('%H:%M:%S')}"

    @property
    def get_updated_at(self):
        return f"{self.updated_at.date()} {self.updated_at.strftime('%H:%M:%S')}"

    @property
    def customer_name(self):
        return self.customer.name if self.customer else ""

    def __str__(self):
        return f"{self.customer.name} avatar" if self.customer else f"avatar {self.id}"


class Note(models.Model):
    description = models.TextField()
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    last = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_created_at(self):
        return f"{self.created_at.date()} {self.created_at.strftime('%H:%M:%S')}"

    @property
    def get_updated_at(self):
        return f"{self.updated_at.date()} {self.updated_at.strftime('%H:%M:%S')}"

    @property
    def customer_name(self):
        return self.customer.name if self.customer else ""

    def __str__(self):
        return f"{self.customer.name} note" if self.customer else f"note {self.id}"


class DriverLicence(models.Model):
    image = models.ImageField(
        upload_to="passports", null=True, blank=True, default=None
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_created_at(self):
        return f"{self.created_at.date()} {self.created_at.strftime('%H:%M:%S')}"

    @property
    def get_updated_at(self):
        return f"{self.updated_at.date()} {self.updated_at.strftime('%H:%M:%S')}"

    @property
    def customer_name(self):
        return self.customer.name if self.customer else ""

    def __str__(self):
        return (
            f"{self.customer.name} passport/DL"
            if self.customer
            else f"passport {self.id}"
        )

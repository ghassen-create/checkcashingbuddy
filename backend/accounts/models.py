from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group, AbstractUser, Permission
from django.db import models

from store.models import Store


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True, default=None)
    store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.SET_NULL)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.username

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url

        from django.templatetags.static import static

        return static("defaults/avatardefault.jpg")

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def store_name(self):
        return self.store.name if self.store else ""

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_date_joined(self):
        return (
            f"{self.date_joined.date()} {self.date_joined.strftime('%H:%M:%S')}"
            if self.date_joined
            else ""
        )

    @property
    def get_last_login(self):
        return (
            f"{self.last_login.date()} {self.last_login.strftime('%H:%M:%S')}"
            if self.last_login
            else ""
        )

    @property
    def get_updated_at(self):
        return (
            f"{self.updated_at.date()} {self.updated_at.strftime('%H:%M:%S')}"
            if self.updated_at
            else ""
        )

import django_filters
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from accounts.models import User


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="username", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="email", lookup_expr="icontains")
    first_name = django_filters.CharFilter(
        field_name="first_name", lookup_expr="icontains"
    )
    last_name = django_filters.CharFilter(
        field_name="last_name", lookup_expr="icontains"
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class GroupFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Group
        fields = ["name"]


class PermissionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    codename = django_filters.CharFilter(field_name="codename", lookup_expr="icontains")
    content_type = django_filters.CharFilter(
        field_name="content_type", method="filter_content_type"
    )

    @staticmethod
    def filter_content_type(queryset, name, value):
        app_label, model = value.split(".")
        content_type = ContentType.objects.get(app_label=app_label, model=model)
        return queryset.filter(content_type=content_type)

    class Meta:
        model = Permission
        fields = ["name", "codename", "content_type"]

# Generated by Django 4.2 on 2023-05-02 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_store_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="store",
            name="user",
        ),
    ]

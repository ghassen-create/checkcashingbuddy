# Generated by Django 4.2 on 2023-05-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("check", "0002_alter_check_commission"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="commission",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=6, max_digits=5, null=True
            ),
        ),
    ]

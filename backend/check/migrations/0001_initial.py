# Generated by Django 4.2 on 2023-05-02 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=5)),
                ('front_image', models.ImageField(upload_to='check_images/')),
                ('back_image', models.ImageField(upload_to='check_images/')),
                ('scanned_by_admin', models.BooleanField(default=False)),
                ('scanned_by_store', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checks', to='customer.customer')),
            ],
        ),
    ]

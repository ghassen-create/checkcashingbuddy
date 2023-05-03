# Generated by Django 4.2 on 2023-05-03 09:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_store_address_store_created_at_store_phone_and_more'),
        ('check', '0003_alter_check_commission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='check',
            name='scanned_by_admin',
        ),
        migrations.RemoveField(
            model_name='check',
            name='scanned_by_store',
        ),
        migrations.AddField(
            model_name='check',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.store'),
        ),
        migrations.AddField(
            model_name='check',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
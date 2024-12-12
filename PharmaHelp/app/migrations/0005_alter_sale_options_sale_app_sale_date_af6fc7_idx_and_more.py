# Generated by Django 5.1.4 on 2024-12-07 05:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_sale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-date']},
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['-date'], name='app_sale_date_af6fc7_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['payment_method'], name='app_sale_payment_4015e5_idx'),
        ),
    ]
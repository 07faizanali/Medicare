# Generated by Django 3.1 on 2023-09-23 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0003_auto_20230922_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='email_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='Email_id'),
        ),
    ]
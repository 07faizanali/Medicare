# Generated by Django 3.1 on 2023-09-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_userdetails_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
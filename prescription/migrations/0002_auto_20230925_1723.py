# Generated by Django 3.1 on 2023-09-25 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20230925_1459'),
        ('prescription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='Email_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.userdetails', to_field='Email_id'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_workers_employee_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-29 22:23

import cuore.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuore', '0002_auto_20210328_2248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functionality',
            options={'verbose_name_plural': 'Functionalities'},
        ),
        migrations.AlterModelOptions(
            name='invoicingdata',
            options={'verbose_name_plural': 'Invoicing data'},
        ),
        migrations.AlterField(
            model_name='activeinvoice',
            name='number',
            field=models.CharField(default=cuore.models.get_invoice_number, max_length=255),
        ),
        migrations.AlterField(
            model_name='default',
            name='key',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

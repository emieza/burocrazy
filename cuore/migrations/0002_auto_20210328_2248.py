# Generated by Django 3.1.7 on 2021-03-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeinvoice',
            name='irpf',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=4),
        ),
        migrations.AlterField(
            model_name='activeinvoice',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='activeinvoice',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=21, max_digits=4),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=21, max_digits=4),
        ),
        migrations.AlterField(
            model_name='customeroffer',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='functionality',
            name='average_hourly_effort',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='functionality',
            name='average_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='functionality',
            name='customer_vat',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='functionality',
            name='worker_vat',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='offerfunctionalityworker',
            name='estimated_hourly_effort',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='offerfunctionalityworker',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='offerfunctionalityworker',
            name='worked_hourly_effort',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='passiveinvoice',
            name='irpf',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=4),
        ),
        migrations.AlterField(
            model_name='passiveinvoice',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='passiveinvoice',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=21, max_digits=4),
        ),
        migrations.AlterField(
            model_name='worker',
            name='default_irpf',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=4),
        ),
        migrations.AlterField(
            model_name='worker',
            name='default_vat',
            field=models.DecimalField(decimal_places=2, default=21, max_digits=4),
        ),
        migrations.AlterField(
            model_name='worker',
            name='hourly_personal_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='workeroffer',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='workertype',
            name='hourly_base_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-28 22:23

from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('internal_notes', models.TextField(blank=True)),
                ('vat', models.DecimalField(decimal_places=2, default=21, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', djrichtextfield.models.RichTextField()),
                ('date_sent', models.DateField(blank=True, null=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Default',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Functionality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', djrichtextfield.models.RichTextField()),
                ('average_hourly_effort', models.DecimalField(decimal_places=1, max_digits=3)),
                ('is_visible_on_offer', models.BooleanField(default=True)),
                ('average_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('worker_vat', models.DecimalField(decimal_places=2, max_digits=2)),
                ('customer_vat', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='InvoicingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('street', models.CharField(blank=True, help_text='Include street and number.', max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=5, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(max_length=128)),
                ('vat_code', models.CharField(blank=True, max_length=128, null=True)),
                ('iban', models.CharField(blank=True, help_text='Bank account number.', max_length=64, null=True)),
                ('swift', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', djrichtextfield.models.RichTextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('internal_notes', models.TextField(blank=True, null=True)),
                ('hourly_personal_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('default_vat', models.DecimalField(decimal_places=2, default=21, max_digits=2)),
                ('default_irpf', models.DecimalField(decimal_places=2, default=15, max_digits=2)),
                ('invoicing_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cuore.invoicingdata')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('hourly_base_rate', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', djrichtextfield.models.RichTextField()),
                ('date_received', models.DateField(blank=True, null=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('file', models.FileField(blank=True, null=True, upload_to='worker_offers')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.project')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.worker')),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='worker_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.workertype'),
        ),
        migrations.CreateModel(
            name='PassiveInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('description', djrichtextfield.models.RichTextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('vat', models.DecimalField(decimal_places=2, default=21, max_digits=2)),
                ('irpf', models.DecimalField(decimal_places=2, default=15, max_digits=2)),
                ('file', models.FileField(blank=True, null=True, upload_to='worker_invoices')),
                ('invoicing_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cuore.invoicingdata')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.project')),
                ('worker_offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cuore.workeroffer')),
            ],
        ),
        migrations.CreateModel(
            name='OfferFunctionalityWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_hourly_effort', models.DecimalField(decimal_places=1, max_digits=3)),
                ('worked_hourly_effort', models.DecimalField(decimal_places=1, max_digits=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('functionality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.functionality')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.customeroffer')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.worker')),
            ],
        ),
        migrations.AddField(
            model_name='customeroffer',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.project'),
        ),
        migrations.AddField(
            model_name='customer',
            name='invoicing_data',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cuore.invoicingdata'),
        ),
        migrations.CreateModel(
            name='ActiveInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('description', djrichtextfield.models.RichTextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('vat', models.DecimalField(decimal_places=2, default=21, max_digits=2)),
                ('irpf', models.DecimalField(decimal_places=2, default=15, max_digits=2)),
                ('customer_offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cuore.customeroffer')),
                ('invoicing_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cuore.invoicingdata')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuore.project')),
            ],
        ),
    ]
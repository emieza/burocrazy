from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.

class Defaults(models.Model):
	key = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

class WorkerType(models.Model):
	name = models.CharField(max_length=128)
	hourly_base_rate = models.DecimalField(max_digits=3,decimal_places=2)

class Address(models.Model):
	name = models.CharField(max_length=255)
	street = models.CharField(max_length=255,help_text="Include street and number.")
	zipcode = models.CharField(max_length=5)
	city = models.CharField(max_length=128)
	country = models.CharField(max_length=128)
	vat_code = models.CharField(max_length=128)

class Worker(models.Model):
	name = models.CharField(max_length=255)
	worker_type = models.ForeignKey(WorkerType,on_delete=models.CASCADE)
	internal_notes = models.TextField(blank=True)
	hourly_personal_rate = models.DecimalField(max_digits=3,decimal_places=2)
	invoicing_data = models.ForeignKey(Address,on_delete=models.CASCADE)
	default_vat = models.DecimalField(max_digits=2,decimal_places=2)
	default_irpf = models.DecimalField(max_digits=2,decimal_places=2)

class Customer(models.Model):
	name = models.CharField(max_length=255)
	internal_notes = models.TextField(blank=True)
	invoicing_data = models.ForeignKey(Address,on_delete=models.CASCADE)
	vat = models.DecimalField(max_digits=2,decimal_places=2)

class Project(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class CustomerOffer(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	date_sent = models.DateField(null=True,blank=True)
	date_approved = models.DateField(null=True,blank=True)
	price = models.DecimalField(max_digits=6,decimal_places=2)

class WorkerOffer(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
	date_approved = models.DateField(null=True,blank=True)
	price = models.DecimalField(max_digits=6,decimal_places=2)


#class ActiveInvoice
#class PassiveInvoice


class Functionality(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	average_hourly_effort = models.DecimalField(max_digits=3,decimal_places=1)
	is_visible_on_offer = models.BooleanField(default=True)
	average_price = models.DecimalField(max_digits=6,decimal_places=2)
	worker_vat = models.DecimalField(max_digits=2,decimal_places=2)
	customer_vat = models.DecimalField(max_digits=2,decimal_places=2)

class OfferFunctionalityWorker(models.Model):
	offer = models.ForeignKey(CustomerOffer,on_delete=models.CASCADE)
	functionality = models.ForeignKey(Functionality,on_delete=models.CASCADE)
	worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
	estimated_hourly_effort = models.DecimalField(max_digits=3,decimal_places=1)
	worked_hourly_effort = models.DecimalField(max_digits=3,decimal_places=1)
	price = models.DecimalField(max_digits=6,decimal_places=2)


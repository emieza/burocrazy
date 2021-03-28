from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.

class Default(models.Model):
	key = models.CharField(max_length=255)
	value = models.CharField(max_length=255)
	def __str__(self):
		return self.key

class WorkerType(models.Model):
	name = models.CharField(max_length=128)
	hourly_base_rate = models.DecimalField(max_digits=5,decimal_places=2)
	def __str__(self):
		return self.name

class InvoicingData(models.Model):
	name = models.CharField(max_length=255)
	street = models.CharField(max_length=255,null=True,blank=True,
								help_text="Include street and number.")
	zipcode = models.CharField(max_length=5,null=True,blank=True)
	city = models.CharField(max_length=128,null=True,blank=True)
	country = models.CharField(max_length=128)
	vat_code = models.CharField(max_length=128,null=True,blank=True)
	iban = models.CharField(max_length=64,null=True,blank=True,
							help_text="Bank account number.")
	swift = models.CharField(max_length=10,null=True,blank=True)
	def __str__(self):
		return "{} - {} - [{}]".format(self.name,self.vat_code,self.id)

class Worker(models.Model):
	name = models.CharField(max_length=255)
	worker_type = models.ForeignKey(WorkerType,on_delete=models.CASCADE)
	internal_notes = models.TextField(null=True,blank=True)
	hourly_personal_rate = models.DecimalField(max_digits=5,decimal_places=2)
	invoicing_data = models.OneToOneField(InvoicingData,on_delete=models.CASCADE)
	default_vat = models.DecimalField(max_digits=4,decimal_places=2,default=21)
	default_irpf = models.DecimalField(max_digits=4,decimal_places=2,default=15)
	def __str__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField(max_length=255)
	company = models.CharField(max_length=255,null=True,blank=True)
	internal_notes = models.TextField(blank=True)
	invoicing_data = models.OneToOneField(InvoicingData,on_delete=models.CASCADE)
	vat = models.DecimalField(max_digits=4,decimal_places=2,default=21)
	def __str__(self):
		return "{} ({})".format(self.name,self.company)

class Project(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class CustomerOffer(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	date_sent = models.DateField(null=True,blank=True)
	date_approved = models.DateField(null=True,blank=True)
	price = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
	def __str__(self):
		return "[{}] {}".format(self.project,self.name)

class WorkerOffer(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	date_received = models.DateField(null=True,blank=True)
	date_approved = models.DateField(null=True,blank=True)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	file = models.FileField(upload_to="worker_offers",null=True,blank=True)
	def __str__(self):
		return "[{}] {} - {}".format(self.project,self.worker,self.name)

class ActiveInvoice(models.Model):
	number = models.CharField(max_length=255)
	date = models.DateField()
	customer_offer = models.OneToOneField(CustomerOffer,on_delete=models.CASCADE)
	# TODO: review include items in model
	invoicing_data = models.OneToOneField(InvoicingData,on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = RichTextField()
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
	vat = models.DecimalField(max_digits=4,decimal_places=2,default=21)
	irpf = models.DecimalField(max_digits=4,decimal_places=2,default=15)
	def __str__(self):
		return self.number

class PassiveInvoice(models.Model):
	number = models.CharField(max_length=255)
	date = models.DateField()
	worker_offer = models.OneToOneField(WorkerOffer,on_delete=models.CASCADE)
	# TODO: review include items in model
	invoicing_data = models.OneToOneField(InvoicingData,on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = RichTextField()
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
	vat = models.DecimalField(max_digits=4,decimal_places=2,default=21)
	irpf = models.DecimalField(max_digits=4,decimal_places=2,default=15)
	file = models.FileField(upload_to="worker_invoices",null=True,blank=True)
	def __str__(self):
		return self.number

class Functionality(models.Model):
	name = models.CharField(max_length=255)
	description = RichTextField()
	average_hourly_effort = models.DecimalField(max_digits=5,decimal_places=1)
	is_visible_on_offer = models.BooleanField(default=True)
	average_price = models.DecimalField(max_digits=8,decimal_places=2)
	worker_vat = models.DecimalField(max_digits=4,decimal_places=2)
	customer_vat = models.DecimalField(max_digits=4,decimal_places=2)
	def __str__(self):
		return self.name

class OfferFunctionalityWorker(models.Model):
	offer = models.ForeignKey(CustomerOffer,on_delete=models.CASCADE)
	functionality = models.ForeignKey(Functionality,on_delete=models.CASCADE)
	worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
	estimated_hourly_effort = models.DecimalField(max_digits=5,decimal_places=1)
	worked_hourly_effort = models.DecimalField(max_digits=5,decimal_places=1)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	def __str__(self):
		return "{} - {} - {}".format(self.offer,self.funcionality,self.worker)


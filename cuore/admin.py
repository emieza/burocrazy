from django.contrib import admin

# Register your models here.

from cuore.models import *


@admin.register(Default)
class DefaultAdmin(admin.ModelAdmin):
	list_display = ("key","value",)

@admin.register(WorkerType)
class WorkerTypeAdmin(admin.ModelAdmin):
	list_display = ("name","hourly_base_rate",)

@admin.register(InvoicingData)
class InvoicingDataAdmin(admin.ModelAdmin):
	pass

class InvoiceDataInline(admin.StackedInline):
	model = InvoicingData

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
	list_display = ("name","worker_type","hourly_personal_rate",)
	#inlines = [ InvoiceDataInline, ]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ("name","company",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("name","customer",)

@admin.register(CustomerOffer)
class CustomerOfferAdmin(admin.ModelAdmin):
	pass

@admin.register(WorkerOffer)
class WorkerOfferAdmin(admin.ModelAdmin):
	pass

@admin.register(ActiveInvoice)
class ActiveInvoiceAdmin(admin.ModelAdmin):
	pass

@admin.register(PassiveInvoice)
class PassiveInvoiceAdmin(admin.ModelAdmin):
	pass

@admin.register(Functionality)
class FunctionalityAdmin(admin.ModelAdmin):
	pass

@admin.register(OfferFunctionalityWorker)
class OfferFunctionalityWorkerAdmin(admin.ModelAdmin):
	pass

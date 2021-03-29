from django.contrib import admin

# Register your models here.
# Reorder elements: https://pypi.org/project/django-modeladmin-reorder/

from cuore.models import *

admin.site.site_header = "Project Burocrazy Management Tool"

@admin.register(Default)
class DefaultAdmin(admin.ModelAdmin):
	list_display = ("key","value",)

@admin.register(WorkerType)
class WorkerTypeAdmin(admin.ModelAdmin):
	list_display = ("name","hourly_base_rate",)

@admin.register(InvoicingData)
class InvoicingDataAdmin(admin.ModelAdmin):
	list_display = ("__str__","vat_code",)

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


class OfferFunctionalityWorkerInline(admin.TabularInline):
	model = OfferFunctionalityWorker

@admin.register(CustomerOffer)
class CustomerOfferAdmin(admin.ModelAdmin):
	list_display = ("name","project","date_sent","date_approved","price",)
	inlines = [ OfferFunctionalityWorkerInline, ]


@admin.register(WorkerOffer)
class WorkerOfferAdmin(admin.ModelAdmin):
	list_display = ("name","project","worker","date_received","date_approved","price",)

@admin.register(ActiveInvoice)
class ActiveInvoiceAdmin(admin.ModelAdmin):
	list_display = ("number","date","issuer","customer","name","customer_offer","price",)
	def save_model(self, request, obj, form, change):
		super().save_model(request, obj, form, change)
		# increment next active invoice number
		defaults = Default.objects.filter(key=INVOICE_NUMBER_KEY)
		next_number = defaults[0]
		current_number = next_number.value
		next_number.value = (str) (int(current_number)+1)
		next_number.save()

@admin.register(PassiveInvoice)
class PassiveInvoiceAdmin(admin.ModelAdmin):
	list_display = ("number","date","project","name","worker_offer","price",)

@admin.register(Functionality)
class FunctionalityAdmin(admin.ModelAdmin):
	list_display = ("name","average_hourly_effort","average_price","is_visible_on_offer",)

@admin.register(OfferFunctionalityWorker)
class OfferFunctionalityWorkerAdmin(admin.ModelAdmin):
	list_display = ("__str__","offer","functionality","worker","estimated_hourly_effort","worked_hourly_effort","price",)

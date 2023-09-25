from django.contrib import admin
from .models import Prescription
# Register your models here.


class PrescriptionAdmin(admin.ModelAdmin):

    list_display =('pres_id','Email_id','pres_image')
    list_display_links =('pres_id','Email_id','pres_image')
    ordering =('-pres_id',)
admin.site.register(Prescription, PrescriptionAdmin)
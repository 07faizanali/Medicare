from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display =('P_id','P_name','Category','P_image','P_quantity','P_details','Price')
    list_display_links =('P_id','P_name','Category','P_image','P_quantity','P_details','Price')
    ordering =('-P_id',)
admin.site.register(Product, ProductAdmin)
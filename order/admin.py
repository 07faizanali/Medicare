from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):

    list_display =('order_id','pay_id','p_id','email_id', 'quantity','amount','shipp_address','order_date')
    list_display_links =('order_id','pay_id','p_id','email_id', 'quantity','amount','shipp_address')
    ordering =('-order_id',)
admin.site.register(Order, OrderAdmin)
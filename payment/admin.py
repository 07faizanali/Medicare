from django.contrib import admin
from .models import Payment
# Register your models here.


class PaymentAdmin(admin.ModelAdmin):

    list_display =('pay_id','p_id','email_id','amount','pay_mode','card_no','exp_month','exp_year','cvv','h_name','pay_date')
    list_display_links =('pay_id','p_id','email_id','amount','pay_mode','card_no','exp_month','exp_year','cvv','h_name')
    ordering =('-pay_id',)
admin.site.register(Payment, PaymentAdmin)
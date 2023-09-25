from django.contrib import admin
from .models import AddToCart

class CartAdmin(admin.ModelAdmin):

    list_display =('cart_id','p_id','p_name','p_image','p_quantity','price','email_id')
    list_display_links =('cart_id','p_id','p_name','p_image','p_quantity','price','email_id' )
    
    ordering =('-cart_id',)

admin.site.register(AddToCart, CartAdmin)
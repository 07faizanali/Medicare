from django.db import models
from registration.models import UserDetails # If you're using Django's built-in User model
from product.models import Product
# Create your models here.

  

class AddToCart(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE, to_field='P_id')
    email_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, to_field='Email_id')  # Assuming you're using Django's built-in User model
    p_name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    p_image = models.CharField(max_length=30, null=False)
    p_quantity = models.IntegerField(null=False)

    def __str__(self):
        return f"Cart {self.cart_id} - {self.p_name}"
    
    class Meta:
        db_table = 'add_to_cart'

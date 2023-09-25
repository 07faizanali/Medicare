from django.db import models
from product.models import Product
from registration.models import UserDetails
from payment.models import Payment
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    pay_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    email_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, to_field='Email_id')
    shipp_address = models.CharField(max_length=100)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    order_date= models.DateTimeField(max_length=30)

    def __str__(self):
        return self.order_id
    

    class Meta:
        db_table='orders'
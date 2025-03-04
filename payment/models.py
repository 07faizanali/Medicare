from django.db import models
from product.models import Product
from registration.models import UserDetails

# Create your models here.
class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    email_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, to_field='Email_id')
    amount = models.IntegerField()
    pay_mode = models.CharField(max_length=20)
    card_no = models.CharField(max_length=20)
    h_name = models.CharField(max_length=30)
    exp_month = models.CharField(max_length=10)
    exp_year = models.IntegerField()
    cvv = models.IntegerField()
    pay_date = models.DateField(max_length=25)

    def __str__(self):
        return self.pay_id
    
    class Meta:
        db_table= 'payment'


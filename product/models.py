from django.db import models

# Create your models here.


class Product(models.Model):
    P_id  = models.AutoField(primary_key=True)
    P_name = models.CharField(max_length=50,null=True)
    Category = models.CharField(max_length=40,null=True)
    P_quantity = models.CharField(max_length=5,null=True)
    P_details = models.TextField(max_length=1500,null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    P_image       = models.ImageField(upload_to='photos/products')
    rating = models.IntegerField(default=0)  # Rating from 0 to 5


    def __str__(self):
        return self.P_name
    
    class Meta:
        db_table = 'product'


        

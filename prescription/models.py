from django.db import models
from registration.models import UserDetails
# Create your models here.
class Prescription(models.Model):
    pres_id = models.AutoField(primary_key=True)
    Email_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, to_field='Email_id')
    pres_image = models.ImageField(upload_to='prescriptions/')


    def __str__(self):
        return self.pres_id
    
    class Meta:
        db_table = 'prescription'
from django.db import models

class Admin(models.Model):
    Admin_id = models.AutoField(primary_key=True)
    Admin_Name = models.CharField(max_length=40)
    Email_id = models.EmailField(unique=True)
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Email_id

     
    class Meta:
        db_table= 'admin'
# Create your models here.

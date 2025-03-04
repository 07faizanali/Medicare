from django.db import models

class AdminAccount(models.Model):
    Admin_id = models.AutoField(primary_key=True)
    AdminName = models.CharField(max_length=40 , null=False)
    Email_id = models.EmailField(max_length=40, unique=True, null=False)
    Password = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.AdminName
    
    class Meta:
        db_table= 'admins'
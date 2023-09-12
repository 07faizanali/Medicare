from django.db import models
from registration.models import UserDetails

# Create your models here.
class Feedback(models.Model):
    F_id = models.AutoField(primary_key=True)
    Email_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, to_field='Email_id')
    Services = models.CharField(max_length=10 , null=False)
    Comment = models.TextField(max_length=150, null=False)
    
    

    def __str__(self):
        return self.F_id
    
    class Meta:
        db_table = 'feedback'
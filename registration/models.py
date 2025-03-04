from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, Email_id, password=None):
        if not Email_id:
            raise ValueError("The Email field must be set")
        Email_id= self.normalize_email(Email_id)
        user = self.model(Email_id=Email_id)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, Email_id, password=None):
        user = self.create_user(Email_id, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 
# Create your models here.
class UserDetails(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40 , null=False)
    Gender = models.CharField(max_length=10 , null=False)
    Address = models.CharField(max_length=50, null=False)
    City = models.CharField(max_length=20, null=False)
    Mobile = models.IntegerField(default='15')
    Email_id = models.EmailField(max_length=40, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    # Add the last_login field
    last_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager() 

    USERNAME_FIELD = "Email_id"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.Email_id
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, add_label):
        return True

    class Meta:
        db_table = 'userdetails'

    



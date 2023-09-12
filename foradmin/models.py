from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class AdminUserManager(BaseUserManager):
    def create_superuser(self, email_id, admin_name, password=None):
        if not email_id:
            raise ValueError("The Email field must be set")
        email_id = self.normalize_email(email_id)
        admin_user = self.model(email_id=email_id, admin_name=admin_name)
        admin_user.set_password(password)
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.save(using=self._db)
        return admin_user

class AdminUser(AbstractBaseUser):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=40, null=False)
    email_id = models.EmailField(max_length=40, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    

    objects = AdminUserManager()

    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = ['admin_name']

    def set_password(self, raw_password):
        self.password = raw_password

    def check_password(self, raw_password):
        return self.password == raw_password

    def __str__(self):
        return self.email_id

    class Meta:
        db_table = 'admin'
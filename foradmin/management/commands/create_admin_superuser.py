from django.core.management.base import BaseCommand
from foradmin.models import AdminUser

class Command(BaseCommand):
    help = 'Create a superuser for the admin app'

    def handle(self, *args, **kwargs):
        email = input('Enter superuser email: ')
        admin_name = input('Enter superuser name: ')
        password = input('Enter superuser password: ')

        if not AdminUser.objects.filter(email_id=email).exists():
            AdminUser.objects.create_superuser(email_id=email, admin_name=admin_name, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists!'))

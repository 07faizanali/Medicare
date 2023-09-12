# from django.contrib.auth.backends import ModelBackend
# from .models import AdminUser

# class AdminUserBackend(ModelBackend):
#     def authenticate(self, request, email_id=None, password=None, **kwargs):
#         try:
#             admin_user = AdminUser.objects.get(email_id=email_id)
#             if admin_user.check_password(password):
#                 return admin_user
#         except AdminUser.DoesNotExist:
#             return None

#     def get_user(self, admin_id):
#         try:
#             return AdminUser.objects.get(pk=admin_id)
#         except AdminUser.DoesNotExist:
#             return None

from django.contrib import admin
from .models import UserDetails

# Register your models here.

class UserDetailsAdmin(admin.ModelAdmin):

    list_display =('user_id','Name','Email_id','Gender','Address','City','Mobile','password','is_active','is_staff')
    list_display_links =('user_id','Name','Gender','Address','City','Mobile','Email_id' )
    readonly_fields= ('password',)
    ordering =('-user_id',)

    filter_horizontal =()
    list_filter =()
    fieldsets =()


# Register your models here.
admin.site.register(UserDetails,UserDetailsAdmin)
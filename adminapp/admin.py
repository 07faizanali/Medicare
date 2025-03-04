from django.contrib import admin
from .models import AdminAccount

class AccountAdmin(admin.ModelAdmin):

    list_display =('Admin_id','AdminName','Email_id','Password')
    list_display_links =('Admin_id','AdminName','Email_id')
    readonly_fields= ('Password',)
    ordering =('-Admin_id',)

admin.site.register(AdminAccount, AccountAdmin)    
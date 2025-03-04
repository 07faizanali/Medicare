from django.contrib import admin
from .models import Feedback
# Register your models here.


class FeedbackAdmin(admin.ModelAdmin):

    list_display =('F_id','Email_id','Services','Comment')
    list_display_links =('F_id','Email_id','Services','Comment')
    ordering =('-F_id',)
admin.site.register(Feedback, FeedbackAdmin)
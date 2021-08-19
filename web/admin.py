from django.contrib import admin
from .models import User_data
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email_address")

admin.site.register(User_data, UserAdmin)
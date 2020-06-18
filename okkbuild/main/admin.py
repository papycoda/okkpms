from django.contrib import admin
from .models import user_login


class loginAdmin(admin.ModelAdmin):
    fields = ["login_id","first_name" ,"last_name","email","password",'department','role']
    readonly_fields = ["created_at","updated_at"]

# Register your models here.
admin.site.register(user_login,loginAdmin)


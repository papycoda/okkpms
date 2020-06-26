from django.contrib import admin
from .models import user_login,payroll_db


class loginAdmin(admin.ModelAdmin):
    fields = ["first_name" ,"last_name","email","password",'department','role']
    readonly_fields = ["login_id","created_at","updated_at"]


class payrollAdmin (admin.ModelAdmin):
    fields = ['TNO','user_Id','username','position',"employee_id", "employee_name",'salary_year','salary_month', "paye", "CUG", 'loan', 'empl_pension', 'total_ded','incentive','net_pay','comment',
              ]


# Register your models here.
admin.site.register(user_login,loginAdmin)
admin.site.register(payroll_db,payrollAdmin)


from django.db import models
from datetime import datetime


# Create your models here.
class user_info(models.Model):
    user_category = models.CharField(max_length=200)
    user_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.user_category

roles = (
         ('user','User')
         ('hro','HRO')
         ('pso','PSO')
         ('hrm','HRM')
         ('hos','HOS')
         ('admin','Admin')
         ('pm','PM')
)
class user_login(models.Model):
    login_id = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45, null = True)
    last_name = models.CharField(max_length=45,null = True)
    email = models.CharField(max_length=100,default='test@okkgrl.com')
    department = models.CharField(max_length=45, null=True)
    role = models.CharField(max_length=6, choices=roles, default='green')
    password = models.CharField(max_length=200,default='test')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.login_id


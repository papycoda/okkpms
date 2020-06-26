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
         ('user','User'),
         ('hro','HRO'),
         ('pso','PSO'),
         ('hrm','HRM'),
         ('hos','HOS'),
         ('admin','Admin'),
         ('pm','PM')
)
class user_login(models.Model):
    login_id = models.CharField(max_length=45, null = True)
    user_Id = models.CharField(max_length=45,primary_key=True)
    username = models.CharField(max_length=45, null=True)
    first_name = models.CharField(max_length=45, null = True)
    last_name = models.CharField(max_length=45,null = True)
    email = models.CharField(max_length=100,default='test@okkgrl.com')
    department = models.CharField(max_length=45, null=True)
    role = models.CharField(max_length=6, choices=roles, default='user')
    password = models.CharField(max_length=200,default='test')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


months = (
         ('january','JANUARY'),
         ('february','FEBRUARY'),
         ('March','MARCH'),
         ('april','APRIL'),
         ('may','MAY'),
         ('june','JUNE'),
         ('july','JULY'),
         ('august','AUGUST'),
         ("september","SEPTEMBER"),
         ("october","OCTOBER"),
         ("november","NOVEMBER"),
         ("december","DECEMBER"),
)

YEAR_CHOICES = []
for r in range(1950, (datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class payroll_db(models.Model):
    employee_id = models.CharField(max_length=45, null = True)
    employee_name = models.CharField(max_length=45, null = True)
    paye = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    CUG = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    loan = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    empl_pension = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    emplc = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    total_ded = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    gross_pay = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    incentive = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    net_pay = models.DecimalField(max_digits=45, null = True,decimal_places=10)
    comment = models.TextField(max_length=500,null = True)
    salary_month = models.CharField('Salary month', max_length=13, choices=months, default='JANUARY')
    salary_year = models.IntegerField('Salary year', choices=YEAR_CHOICES, default=datetime.now().year)
    user_Id = models.ForeignKey(user_login,on_delete=models.CASCADE)
    username = models.CharField(max_length=45, null = True)
    position = models.CharField(max_length=45, null = True)
    TNO = models.PositiveIntegerField(primary_key=True)
    objects = models.Manager()


    # def __str__(self):
    #     return self.login_id


# Generated by Django 2.2.6 on 2020-06-25 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('hro', 'HRO'), ('pso', 'PSO'), ('hrm', 'HRM'), ('hos', 'HOS'), ('admin', 'Admin'), ('pm', 'PM')], default='user', max_length=6),
        ),
        migrations.CreateModel(
            name='payroll_db',
            fields=[
                ('employee_id', models.CharField(max_length=45, null=True)),
                ('employee_name', models.CharField(max_length=45, null=True)),
                ('paye', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('CUG', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('loan', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('empl_pension', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('emplc', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('total_ded', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('gross_pay', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('incentive', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('net_pay', models.DecimalField(decimal_places=10, max_digits=45, null=True)),
                ('comment', models.TextField(max_length=500, null=True)),
                ('salary_year', models.DateField(max_length=45, null=True)),
                ('salary_month', models.DateField(max_length=45, null=True)),
                ('username', models.CharField(max_length=45, null=True)),
                ('position', models.CharField(max_length=45, null=True)),
                ('TNO', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_login')),
            ],
        ),
    ]

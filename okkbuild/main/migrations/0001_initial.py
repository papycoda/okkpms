# Generated by Django 2.2.6 on 2020-06-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_title', models.CharField(max_length=200)),
                ('login_content', models.TextField()),
                ('last_login', models.DateTimeField(verbose_name='last login')),
            ],
        ),
    ]
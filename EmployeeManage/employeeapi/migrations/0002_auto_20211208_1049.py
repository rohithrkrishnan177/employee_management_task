# Generated by Django 3.2.10 on 2021-12-08 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emplyee_name',
            new_name='employee_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emplyee_regNo',
            new_name='employee_regNo',
        ),
    ]

from django.db import models

# Create your models here.
class Department(models.Model):
    dpt_name = models.TextField()

    class Meta:
        db_table = 'departments'


class Employee(models.Model):

    departmentID = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.TextField()
    second_name = models.TextField()
    gender = models.TextField()
    national_id = models.TextField()
    kra_pin = models.TextField()
    email = models.TextField()
    basic_salary = models.TextField()
    allowances = models.TextField()

    class Meta:
        db_table = 'employees'

class Payrolls(models.Model):

    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    payroll_month = models.TextField()
    gross_salary = models.TextField()
    nssf_deductions = models.TextField()
    nhif_deductions = models.TextField()
    taxable_income = models.TextField()
    PAYE = models.TextField()
    overtime = models.TextField()
    salary_advance = models.TextField()
    other_deductions = models.TextField()
    net_salary = models.TextField()

    class Meta:
        db_table = "payrolls"
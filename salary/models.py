from django.db import models
from employee.models import Employee

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    dearness_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    house_rent_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    professional_tax = models.DecimalField(max_digits=10, decimal_places=2)
    tax_deducted = models.DecimalField(max_digits=10, decimal_places=2)
    provident_fund = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee} {self.month}"
from django import forms
from employee.models import Employee
from .models import Salary

class SalaryForm(forms.ModelForm):
    employee = Employee.objects.filter(is_staff=False)   
    class Meta:
        model = Salary
        fields = [
            'employee',
            'month',
            'basic_salary',
            'dearness_allowance',
            'house_rent_allowance',
            'professional_tax',
            'tax_deducted',
            'provident_fund',
            'net_salary'
        ]

    def __init__(self, *args, **kwargs):
        super(SalaryForm, self).__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs['class'] = 'form-control'
        self.fields['employee'].widget.attrs['placeholder'] = 'Select Employee'
        self.fields['month'].widget.attrs['class'] = 'form-control'
        self.fields['month'].widget.attrs['placeholder'] = 'Select Month'
        self.fields['basic_salary'].widget.attrs['class'] = 'form-control'
        self.fields['basic_salary'].widget.attrs['placeholder'] = 'Enter Basic Salary'
        self.fields['dearness_allowance'].widget.attrs['class'] = 'form-control'
        self.fields['dearness_allowance'].widget.attrs['placeholder'] = 'Enter Dearness Allowance'
        self.fields['house_rent_allowance'].widget.attrs['class'] = 'form-control'
        self.fields['house_rent_allowance'].widget.attrs['placeholder'] = 'Enter House Rent'
        self.fields['professional_tax'].widget.attrs['class'] = 'form-control'
        self.fields['professional_tax'].widget.attrs['placeholder'] = 'Enter Professional Tax'
        self.fields['tax_deducted'].widget.attrs['class'] = 'form-control'
        self.fields['tax_deducted'].widget.attrs['placeholder'] = 'Enter Tax Deduction'
        self.fields['provident_fund'].widget.attrs['class'] = 'form-control'
        self.fields['provident_fund'].widget.attrs['placeholder'] = 'Enter Provident Fund'
        self.fields['net_salary'].widget.attrs['class'] = 'form-control'
        self.fields['net_salary'].widget.attrs['placeholder'] = 'Enter Net Salary'
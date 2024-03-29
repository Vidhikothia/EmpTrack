from django.contrib import admin
from django.urls import path
from employee.views import *


urlpatterns = [
    path('', load_dasboard, name=""),
    path('logout', logout_employee, name='logout'),
    path('profile_employee', profile_employee, name='profile_employee'),
    path('profile_admin', profile_admin, name='profile_admin'),
    path('admin_login', login_admin, name="admin_login"),
    path('employee_login', login_employee, name="employee_login"),
    path('employee_registration', employee_registration, name="employee_registration"),
    path('admin_dashboard', admin_dashboard, name="admin_dashboard"),
    path('employee_dashboard', employee_dashboard, name="employee_dashboard"),
]
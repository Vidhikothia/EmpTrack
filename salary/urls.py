from django.urls import path
from .views import *

urlpatterns = [
    
    path('salary_pdf',salary_pdf,name='salary_pdf' ),
    path('add_salary_report',add_salary_report,name='add_salary_report' ),
    
]
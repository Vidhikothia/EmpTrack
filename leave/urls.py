from django.urls import path
from .views import *

urlpatterns = [
    
    path('apply_leave',apply_leave,name='apply_leave' ),
    path('manage_leave',manage_leave, name='manage_leave' ),
    path('leave_approved/<int:id>',leave_approved, name='leave_approved' ),
    path('leave_rejected/<int:id>',leave_rejected, name='leave_rejected' ),
]
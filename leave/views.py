from django.shortcuts import render, redirect
from .models import Leave
from django.contrib.auth.decorators import login_required


@login_required
def manage_leave(request):
    leaves = Leave.objects.all()
    return render(request,'leave/manage_leave.html',{'leaves':leaves})

@login_required
def apply_leave(request):
    if request.method == 'POST':
        employee_id = request.user
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        leave = Leave(employee=employee_id, start_date=start_date, end_date=end_date, reason=reason)
        leave.save()
        return redirect('employee_dashboard')
    context = {'user':request.user}
    return render(request,'leave/apply_leave.html',context)

@login_required
def leave_approved(request,id):
    l_app = Leave.objects.get(id=id)
    l_app.status = 1
    l_app.save()
    return redirect('manage_leave')
    
@login_required
def leave_rejected(request,id):
    l_app = Leave.objects.get(id=id)
    l_app.status = 2
    l_app.save()
    return redirect('manage_leave')
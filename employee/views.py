from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from leave.models import Leave
from .forms import RegistrationForm



def load_dasboard(request):
    return render(request,"employee/load.html")

def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'employee/adminlogin.html', {'error_message': 'Invalid credentials or Employee Rights.'})
    else:
        return render(request,"employee/adminlogin.html")


def login_employee(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect('employee_dashboard')
        else:
            return render(request, 'employee/employeelogin.html', {'error_message': 'Invalid credentials or Admin Rights.'})
    else:
        return render(request,"employee/employeelogin.html")
    

@login_required
def employee_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'employee/employeeregister.html', {'form': form})

@login_required
def admin_dashboard(request):
    leave_data = Leave.objects.filter(status=0)
    return render(request, 'employee/admin_dashboard.html',{'leave_data':leave_data})

@login_required
def profile_employee(request):
    data = request.user
    return render(request, 'employee/employeeprofile.html',{'data':data})

@login_required
def employee_dashboard(request):
    leaves = Leave.objects.filter(employee=request.user)            
    return render(request, 'employee/employee_dashboard.html',{'leaves':leaves})

@login_required
def profile_admin(request):
    data = request.user
    return render(request, 'employee/employeeprofile.html',{'data':data})


@login_required
def logout_employee(request):
    logout(request)
    return redirect('/')
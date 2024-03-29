from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
from django.conf import settings
from django.template.loader import get_template
from django.http import HttpResponse, FileResponse
from employee.models import Employee
from salary.models import Salary
from salary.forms import SalaryForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
import os


def link_callback(uri, rel):
    result = finders.find(uri)
    if result:
            if not isinstance(result, (list, tuple)):
                    result = [result]
            result = list(os.path.realpath(path) for path in result)
            path=result[0]
    else:
            sUrl = settings.STATIC_URL
            sRoot = settings.STATIC_ROOT
            mUrl = settings.MEDIA_URL
            mRoot = settings.MEDIA_ROOT
            if uri.startswith(mUrl):
                    path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                    path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                    return uri
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment filename="report.pdf"'
    html  = template.render(context_dict)
    pisa_status = pisa.CreatePDF(html, dest = response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return FileResponse(response, content_type='application/pdf')


@login_required
def salary_pdf(request):
    if request.method == 'POST':
        user = request.user  
        month_str = request.POST['month1']
        month_with_day = month_str + "-01" 
        month = datetime.strptime(month_with_day, '%Y-%m-%d').date() 
        print(month) 
        user_month_salaries = Salary.objects.get(employee=user,month__year=month.year, month__month=month.month)
        print(user_month_salaries)
        context = {
            'salaries': user_month_salaries,
        }
    return render_to_pdf('salary/salary_pdf.html', context)


@login_required
def add_salary_report(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
              print(form.errors)
    else:
        form = SalaryForm()
    return render(request,'salary/add_salary_report.html',{'form':form})

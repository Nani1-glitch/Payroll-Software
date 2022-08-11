from django.shortcuts import render
from django.http import HttpResponse
from payrolls.models import Department
from payrolls.models import Employee
from payrolls.models import Payrolls


# Create your views here.
def home(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def departments(request):
    if(request.method == 'POST'):
        department = Department(
            dpt_name = request.POST.get("dpt_name")
            )
        department.save()

    departments = Department.objects.all()
    context1 = {
        'departments':departments
    }

    return render(request,'departments.html',context1)
def employees(request):
    if request.method == 'POST':
        employee = Employee(
        departmentID= request.POST.get("departmentID"),
        first_name = request.POST.get("first_name"),
        second_name = request.POST.get("second_name"),
        gender = request.POST.get("gender"),
        national_id = request.POST.get("national_id"),
        kra_pin = request.POST.get("kra_pin"),
        email = request.POST.get("email"),
        basic_salary = request.POST.get("basic_salary"),
        allowances = request.POST.get("allowances")
        )
        employee.save()
    employeees = Employee.objects.all()
    context2 = {
        'employeees': employeees
    }
    departments = Department.objects.all()
    context1 = {
        'departments': departments
    }
    return render(request,'employees.html',context1,context2)
def payrolls(request):
    return render(request,'payrolls.html')

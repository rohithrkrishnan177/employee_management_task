from .forms import EmployeeForm,NumWordForm
from .models import Employee
from django.shortcuts import  render, redirect
from num2words import num2words
import gtts

# Create your views here.



def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_insert(request,id=0):
    if request.method == "GET":
        print(id)
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            print("hehe")
            print(employee)
            form = EmployeeForm(instance=employee)
            if form.is_valid():
                form.save()
                print("abchd", form)
                return redirect('/employee/employee_list')
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            print("@@@@@@@@@@@@@@",form)
            form.save()
            print("1234567876542345678",form)
        return redirect('/employee/employee_list')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    print("asdfgh")
    return redirect('/employee/employee_list')



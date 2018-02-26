from django.shortcuts import render
from django.views import View

from account import models as account_model
from account import forms as account_form


class Home(View):
    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name)



#employee
class Employee(View):
    template_name = 'home/employee.html'

    def get(self, request):
        employee_form = account_form.EmployeeForm()

        employees = account_model.Employee.objects.all()

        variables = {
            'employees': employees,
            'employee_form': employee_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        employee_form = account_form.EmployeeForm(request.POST or None)

        employees = account_model.Employee.objects.all()

        if employee_form.is_valid():
            employee_form.deploy()

        variables = {
            'employees': employees,
            'employee_form': employee_form,
        }

        return render(request, self.template_name, variables)

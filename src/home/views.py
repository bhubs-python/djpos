from django.shortcuts import render
from django.views import View

from account import models as account_view


class Home(View):
    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name)



#employee
class Employee(View):
    template_name = 'home/employee.html'

    def get(self, request):

        employees = account_view.Employee.objects.all()

        variables = {
            'employees': employees,
        }

        return render(request, self.template_name, variables)

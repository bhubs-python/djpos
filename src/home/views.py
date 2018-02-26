from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from account import models as account_model
from account import forms as account_form
from . import serializers


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



#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::API::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#employee api
class EmployeeApi(APIView):
    def get(self, request):
        usr = request.GET.get('usr')

        #make list from text
        user_list = usr.split(',')

        message = False
        for u in user_list:
            emp_obj = account_model.Employee.objects.get(id=u)
            emp_obj.delete()
            message = 'Delete'

        return Response({
            'message': message,

        })

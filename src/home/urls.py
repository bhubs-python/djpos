from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),

    #url for employee
    url(r'^employee/$', views.Employee.as_view(), name='employee'),


    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #:::::::::::::::::::::::api::::::::::::::::::::::::::::::::::::
    url(r'^employee/api/$', views.EmployeeApi.as_view(), name='employee-api'),
]

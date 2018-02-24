from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.views import login, logout
from django.db.models import Q

from . import forms
from . import models


# logout
def logout_request(request):
    logout(request)
    return redirect('account:login')


class Login(View):
    template_name = 'account/login.html'

    def get(self, request):
        loginForm = forms.LoginForm()

        variables = {
            'loginForm': loginForm,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        loginForm = forms.LoginForm(request.POST or None)

        if loginForm.is_valid():
            user = loginForm.login()
            if user:
                login(request, user)
                return redirect('home:index')

        variables = {
            'loginForm': loginForm,
        }

        return render(request, self.template_name, variables)

from django import forms
from django.contrib.auth import authenticate
from django.db.models import Q

import re
from django.utils.timezone import now


from . import models



# login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 1:
            raise forms.ValidationError("Enter Username!")
        else:
            if len(password) < 8:
                raise forms.ValidationError("Password is too short!")
            else:
                user = authenticate(username=username, password=password)
                if not user or not user.is_active:
                    raise forms.ValidationError("Username or Password not matched!")
        return self.cleaned_data

    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user




# login form
gender = (
    ('male', 'Male'),
    ('female', 'Female'),
)

class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    gender = forms.ChoiceField(choices=gender, required=False, widget=forms.Select(attrs={'class': 'validate browser-default'}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    phone_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    address = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))
    city = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    state = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    post_code = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    comment = forms.CharField(required=False, max_length=255, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))




    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')
        address = self.cleaned_data.get('address')
        city = self.cleaned_data.get('city')
        state = self.cleaned_data.get('state')
        post_code = self.cleaned_data.get('post_code')
        comment = self.cleaned_data.get('comment')


        if len(first_name) < 1:
            raise forms.ValidationError("Enter First Name!")
        else:
            if len(last_name) < 1:
                raise forms.ValidationError("Enter Last Name!")
            else:
                email_correction = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
                if email_correction == None:
                    raise forms.ValidationError("Email not correct!")
                else:
                    email_exist = models.Employee.objects.filter(email__iexact=email).exists()
                    if email_exist:
                        raise forms.ValidationError("Email already exist!")


    def deploy(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')
        address = self.cleaned_data.get('address')
        city = self.cleaned_data.get('city')
        state = self.cleaned_data.get('state')
        post_code = self.cleaned_data.get('post_code')
        comment = self.cleaned_data.get('comment')


        deploy = models.Employee(first_name=first_name, last_name=last_name, gender=gender, email=email, phone_number=phone_number, address=address, city=city, state=state, post_code=post_code, comment=comment)
        deploy.save()

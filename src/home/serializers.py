from rest_framework import serializers

from . import models
from account import models as account_model


class EmployeeDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = account_model.Employee
        fields = ('id', 'first_name', )
